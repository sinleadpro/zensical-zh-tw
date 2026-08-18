#!/usr/bin/env python3
"""Validate Zensical docs frontmatter metadata against frontmatter-schema.yaml.

Usage:
    python scripts/validate_docs_frontmatter.py [files...]
    python scripts/validate_docs_frontmatter.py  # validates all docs/**/*.md
"""

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "frontmatter-schema.yaml"
DOCS_DIR = ROOT / "docs"
PERMALINK_BASE_URL = "https://help.cyberbiz.io"


def load_schema():
    with open(SCHEMA_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


FRONTMATTER_RE = re.compile(r"^---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n", re.DOTALL)


def parse_frontmatter(filepath: Path):
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    m = FRONTMATTER_RE.match(content)
    if not m:
        return None, content
    fm_text = m.group(1).strip()
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        return None, content
    return fm, content[m.end() :]


def relative_path(filepath: Path):
    try:
        return filepath.relative_to(ROOT).as_posix()
    except ValueError:
        return Path(filepath).as_posix()


def expected_permalink(filepath: Path):
    rel = filepath.relative_to(DOCS_DIR).as_posix()
    rel = rel.removesuffix(".md")
    if rel == "index":
        return f"{PERMALINK_BASE_URL}/"
    rel = rel.removesuffix("/index")
    return f"{PERMALINK_BASE_URL}/{rel}/"


def _type_error(field_name, expected, value):
    return f"[{field_name}] expected {expected}, got {type(value).__name__}"


def validate_enum(value, field_def, field_name, filepath):
    errors, warnings = [], []
    if not isinstance(value, str):
        errors.append(_type_error(field_name, "string", value))
        return errors, warnings
    valid = field_def.get("values", [])
    if value not in valid:
        errors.append(f"[{field_name}] '{value}' not in enum. Valid: {valid}")
    return errors, warnings


def validate_enum_array(value, field_def, field_name, filepath):
    errors, warnings = [], []
    if not isinstance(value, list):
        errors.append(_type_error(field_name, "array", value))
        return errors, warnings
    valid = field_def.get("values", [])
    for item in value:
        if not isinstance(item, str):
            errors.append(f"[{field_name}] array item must be string, got {type(item).__name__}")
        elif item and item not in valid:
            errors.append(f"[{field_name}] '{item}' not in enum. Valid: {valid}")
    return errors, warnings


def validate_string_array(value, field_def, field_name, filepath):
    errors, warnings = [], []
    if not isinstance(value, list):
        errors.append(_type_error(field_name, "array", value))
        return errors, warnings
    for item in value:
        if not isinstance(item, str):
            errors.append(f"[{field_name}] array item must be string, got {type(item).__name__}")
    return errors, warnings


def validate_url(value, field_def, field_name, filepath):
    errors, warnings = [], []
    if not str(value).startswith(PERMALINK_BASE_URL):
        errors.append(f"[{field_name}] must start with {PERMALINK_BASE_URL}, got: {value}")
        return errors, warnings
    expected = expected_permalink(filepath)
    if value != expected:
        errors.append(f"[{field_name}] '{value}' does not match expected '{expected}'")
    return errors, warnings


def validate_date(value, field_def, field_name, filepath):
    errors, warnings = [], []
    if not isinstance(value, str):
        errors.append(_type_error(field_name, "date string", value))
        return errors, warnings
    fmt = field_def.get("format", "YYYY-MM-DD HH:mm")
    if fmt == "YYYY-MM-DD HH:mm" and not re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$", value):
        errors.append(f"[{field_name}] '{value}' does not match format {fmt}")
    return errors, warnings


def validate_integer(value, field_def, field_name, filepath):
    errors, warnings = [], []
    if not isinstance(value, int) or isinstance(value, bool):
        errors.append(_type_error(field_name, "integer", value))
    return errors, warnings


def validate_boolean(value, field_def, field_name, filepath):
    errors, warnings = [], []
    if not isinstance(value, bool):
        errors.append(_type_error(field_name, "boolean", value))
    return errors, warnings


def validate_string(value, field_def, field_name, filepath):
    errors, warnings = [], []
    if not isinstance(value, str):
        errors.append(_type_error(field_name, "string", value))
        return errors, warnings
    max_len = field_def.get("max_length")
    if max_len and len(value) > max_len:
        warnings.append(f"[{field_name}] {len(value)} chars exceeds recommended {max_len}")
    return errors, warnings


def validate_object(value, field_def, field_name, filepath):
    errors, warnings = [], []
    if not isinstance(value, dict):
        errors.append(_type_error(field_name, "object", value))
        return errors, warnings
    properties = field_def.get("properties", {})
    for prop_name, prop_def in properties.items():
        prop_value = value.get(prop_name)
        prop_type = prop_def.get("type", "string")
        if prop_type == "boolean" and not isinstance(prop_value, bool):
            errors.append(f"[{field_name}.{prop_name}] expected boolean, got {type(prop_value).__name__}")
    return errors, warnings


VALIDATORS = {
    "enum": validate_enum,
    "enum[]": validate_enum_array,
    "string[]": validate_string_array,
    "url": validate_url,
    "date": validate_date,
    "integer": validate_integer,
    "boolean": validate_boolean,
    "string": validate_string,
    "object": validate_object,
}


def validate_field(value, field_def, field_name, filepath, schema):
    errors, warnings = [], []
    required = field_def.get("required", False)

    if required and (value is None or value == "" or (isinstance(value, list) and len(value) == 0)):
        errors.append(f"[{field_name}] is required but missing or empty")
        return errors, warnings

    if value is None or value == "" or (isinstance(value, list) and len(value) == 0):
        return errors, warnings

    ftype = field_def.get("type", "string")
    validator = VALIDATORS.get(ftype)
    if validator:
        e, w = validator(value, field_def, field_name, filepath)
        errors.extend(e)
        warnings.extend(w)

    return errors, warnings


def validate_file(filepath: Path, schema):
    filepath = filepath.resolve()
    fm, content = parse_frontmatter(filepath)
    if fm is None and not content.strip():
        return []
    if fm is None:
        return [("[frontmatter] missing or invalid YAML", "ERROR")]
    results = []
    fields = schema.get("fields", {})
    rel = filepath.relative_to(DOCS_DIR).as_posix()

    for field_name, field_def in fields.items():
        if field_name == "products" and rel.startswith("resources/"):
            continue
        value = fm.get(field_name)
        errors, warnings = validate_field(
            value, field_def, field_name, filepath, schema
        )
        for e in errors:
            results.append((e, "ERROR"))
        for w in warnings:
            results.append((w, "WARNING"))

    for key in fm:
        if key not in fields:
            results.append((f"[{key}] unknown field, not defined in schema", "ERROR"))

    return results


def main():
    schema = load_schema()
    files = sys.argv[1:] if len(sys.argv) > 1 else sorted(DOCS_DIR.rglob("*.md"))

    all_errors = 0
    all_warnings = 0

    for f in files:
        filepath = Path(f) if isinstance(f, str) else f
        if not str(filepath).endswith(".md"):
            continue
        results = validate_file(filepath, schema)
        if results:
            rel = relative_path(filepath)
            print(f"\n{rel}")
            for msg, level in results:
                print(f"  {level}: {msg}")
                if level == "ERROR":
                    all_errors += 1
                else:
                    all_warnings += 1

    print("\n---")
    print(f"Errors: {all_errors}, Warnings: {all_warnings}")

    if all_errors > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
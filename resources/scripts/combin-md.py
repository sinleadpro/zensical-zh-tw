import os

INPUT_DIR = "playground/todo"
OUTPUT_DIR = "playground/done"
OUTPUT_FILE = "combined.md"

def combine_markdown_files():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    md_files = sorted(
        f for f in os.listdir(INPUT_DIR)
        if f.endswith(".md")
    )

    if not md_files:
        print(f"❌ No Markdown files found in '{INPUT_DIR}/'")
        return

    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)

    with open(output_path, "w", encoding="utf-8") as outfile:
        for filename in md_files:
            file_path = os.path.join(INPUT_DIR, filename)

            with open(file_path, "r", encoding="utf-8") as infile:
                content = infile.read().strip()

            outfile.write("\n\n<!-- ================================ -->\n")
            outfile.write(f"<!-- Source: {filename} -->\n")
            outfile.write("<!-- ================================ -->\n\n")
            outfile.write(content)
            outfile.write("\n")

    print(f"✅ Combined {len(md_files)} files into '{output_path}'")

if __name__ == "__main__":
    combine_markdown_files()

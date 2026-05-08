import os

def define_env(env):
    """
    Hook for Zensical Macros to define variables and logic.
    """
    
    # 1. Grab the environment variable from your shell/Cloudflare
    # Defaulting to 'false' ensures your public build is always safe.
    raw_value = os.getenv('INTERNAL_DOCS', 'false').lower()
    
    # 2. Convert the string to a real Python Boolean
    is_internal = (raw_value == 'true')
    
    # 3. Register the variable for use in your Markdown files
    # This allows you to use {% if is_internal %}
    env.variables['is_internal'] = is_internal

    # 4. (Optional) Debugging: This prints in your terminal 
    # to confirm the gate status during 'uv run zensical serve'
    status_icon = "🔓" if is_internal else "🔒"
    print(f"--- Zensical Macro: Internal Gate is {status_icon} ({is_internal}) ---")




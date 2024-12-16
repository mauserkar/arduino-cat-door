def read_env(file_path):
    env_vars = {}
    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                key, value = line.split("=", 1)
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                env_vars[key.strip()] = value.strip()
    except Exception as e:
        print(f"Error reading .env file: {e}")
    return env_vars


env = read_env(".env")

switch_pin_num = 25

import json

CONFIG_FILE = "config.json"

# Default settings
default_settings = {
    "list_length": 20,
    "random_number_upper_limit": 1000,
    "enable_animation": True
}

# Load settings with a fallback to default values
def load_settings():
    global settings
    try:
        with open(CONFIG_FILE, "r") as file:
            settings = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        settings = default_settings.copy()
        save_settings()  # Save the default settings if the config file doesn't exist or is corrupted

def save_settings():
    with open(CONFIG_FILE, "w") as file:
        json.dump(settings, file, indent=4)

# Load settings when the module is imported
load_settings()

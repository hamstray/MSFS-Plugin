import json
import os

PRESETS_FILE = "config/presets.json"

def load_presets():
    if not os.path.exists(PRESETS_FILE):
        return {}
    try:
        with open(PRESETS_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading presets: {e}")
        return {}

def save_presets(presets):
    os.makedirs("config", exist_ok=True)  # Ensure the directory exists
    try:
        with open(PRESETS_FILE, "w") as f:
            json.dump(presets, f, indent=4)
            print("Presets saved successfully.")
    except Exception as e:
        print(f"Error saving presets: {e}")

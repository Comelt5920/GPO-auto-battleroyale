import os
import json

CONFIG_FILE = "config.json"
ASSETS_DIR = os.path.join("src", "assets")
LOG_FILE = "debug_log.txt"

def load_config():
    default_config = {
        "discord_webhook": "",
        "confidence": 0.8,
        "scan_interval": 2.0,
        "match_mode": "full", # New: "full" or "quick"
        "movement_duration": 300,  # 5 minutes in seconds
        "images": {
            "change": "src/assets/change.png",
            "br_mode": "src/assets/br_mode.png",
            "solo_mode": "src/assets/solo_mode.png",
            "return_to_lobby_alone": "src/assets/leave.png",
            "ultimate": "src/assets/ultimate.png",                 
            "open": "src/assets/open.png",
            "continue": "src/assets/continue.png"
        },
        "pos_1": [100, 100],
        "pos_2": [200, 200],
        "outcome_area": None,
        "keys": {
            "menu": "m",
            "slot_1": "1",
            "forward": "w",
            "left": "a",
            "backward": "s",
            "right": "d"
        }
    }
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                user_config = json.load(f)
                
                if "images" in user_config:
                    merged_images = default_config["images"].copy()
                    for k, v in user_config["images"].items():
                        if k in merged_images:
                            merged_images[k] = v
                    user_config["images"] = merged_images
                
                return {**default_config, **user_config}
        except:
            return default_config
    return default_config

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

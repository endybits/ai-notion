import os
import json

file_path = "./config/keys.json"

def get_config_keys():
    return json.loads(open(file_path, "r").read()) if os.path.exists(file_path) else {}
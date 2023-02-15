# ------------------------------
# ARC Drone Competition code
# Main programmer: Stanley Chen
# 
# See ARC_code/README.md for full information
import json
#get config values from config.json
configReader = open("config.json")
config = json.loads(configReader.read())

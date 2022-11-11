# ------------------------------
# ARC Drone Competition code
# Main programmer: Stanley Chen
# 
# See ARC_code/README.md for full information
# ------------------------------
# Import built in modules for all files
import math
import random
import time
import json
# Import MAVSDK library, this library will be actually
# controlling the drone (such as taking off or setting max speed)
from mavsdk import System
# Create a System() object called drone
drone = System()
# Load config settings
f = open("config.json", "r")
# Create a dictionary and parse json from the file into it
config = json.loads(f.read())

# config["max_speed"]

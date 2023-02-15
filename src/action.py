# ------------------------------
# ARC Drone Competition code
# Main programmer: Stanley Chen
# 
# See ARC_code/README.md for full information
# ------------------------------
# To keep everything organized, we will define drone actions in action.py
# Import drone from Main.py 
# import external libraries/built in modules
from main import drone
import time
import config
import asyncio
# Main function for drone
# This function will be all the stuff the drone actually does
async def run():
  try:
    await drone.connect()
  except: 
    print("Unable to connect to drone")
  else: 
    print("Sucessfully connected to drone")
  time.sleep(2)


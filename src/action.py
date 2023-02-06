# ------------------------------
# ARC Drone Competition code
# Main programmer: Stanley Chen
# 
# See ARC_code/README.md for full information
# ------------------------------
# To keep everything organized, we will define drone actions in action.py
# Import drone from Main.py
# Python automatically caches imported modules, so we do not have to 
# import external libraries/built in modules again
import main
import config
import asyncio
async def run():
  try:
    await main.drone.connect()
  except: 
    print("Unable to connect to drone")
  else: 
    print("Sucessfully connected to drone")
  main.time.sleep(2)


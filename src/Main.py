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
import asyncio
# Import MAVSDK library, this library will be actually
# controlling the drone (such as taking off or setting max speed)
from mavsdk import System
# Create a System() object called drone
drone = System()
# The main function
# This should work, as I copied most of it from the official Github repo
async def run():
  # Connect to drone
  await drone.connect(system_address="udp://:14540")
  async for state in drone.core.connection_state():
    if state.is_connected:
      print(f"Drone discovered with UUID: {state.uuid}")
      break
  # 2 second safety margin
  await asyncio.sleep(2)
  # Arm the drone, then let it automatically shut down
  await drone.action.arm()

# Run it  
if __name__ == "__main__":
  loop = asyncio.get_event_loop()
  loop.run_until_complete(run())

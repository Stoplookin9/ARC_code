# ------------------------------
# ARC Drone Competition code
# Main programmer: Stanley Chen
# 
# See ARC_code/README.md for full information
# ------------------------------
# Import built in modules
import math
import time
# Import MAVSDK library, this library will be actually
# controlling the drone (such as taking off or setting max speed)
from mavsdk import System
# Create a System() object called drone
drone = System()
# Prepare the drone
def init_drone(): 
  # The definition drone.action.arm() commands the drone to spin all motors slowly
  # For safety purposes, we will delay arming by 10 seconds. 
  print("Drone is arming in 10 seconds, please clear area of all objects and personal!")
  time.sleep(5)
  print("Drone is arming in 5 seconds!")
  time.sleep(5)
  print("Drone arming!")
  # Arm the drone
  await drone.action.arm()
  
  
# Commands for test flight
# Note: Drone arming is done seperately in the definition init_drone()
def test_flight:
  time.sleep(3)
  await drone.action.disarm()

init_drone()

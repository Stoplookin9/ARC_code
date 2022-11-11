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
from Main import drone
# Prepare the drone
def arm_drone(): 
  # The function drone.action.arm() commands the drone to spin all motors slowly
  # For safety purposes, we will delay arming by 10 seconds. 
  print("Drone is arming in 10 seconds, please clear area of all objects and personal!")
  time.sleep(5)
  print("Drone is arming in 5 seconds!")
  time.sleep(5)
  print("Drone arming!")
  # Arm the drone
  await drone.action.arm()
  
  
# Commands for test flight
# Note: Drone arming is done seperately in the function init_drone()
def test_flight:
  time.sleep(3)
  await drone.action.disarm()

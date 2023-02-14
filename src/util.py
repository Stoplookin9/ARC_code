# ------------------------------
# ARC Drone Competition code
# Main programmer: Stanley Chen
# 
# See ARC_code/README.md for full information
# ------------------------------
# Utilities for ARC_code
# Import built in modules
import math
import random
# Basic math formulas (self-explanatory)
def getDistance(x1, y1, x2, y2):
  return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
def getDistance3(x1, y1, z1, x2, y2, z2): 
  return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
def getArcLength(radius, theta): 
  return radius * theta;
def degToRad(deg): 
  return deg * math.pi / 180
def radToDeg(rad):
  return rad * 180 / math.pi
# More complex formulas
# Trajectory calculation
def calculateTrajectory(x):

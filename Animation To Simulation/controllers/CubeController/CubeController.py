"""This controller moves the red ball around the robot."""

from math import sin, cos, pi
from controller import Supervisor
import os
import re

supervisor = Supervisor()
timestep = int(supervisor.getBasicTimeStep())

cube = supervisor.getFromDef('CUBE')
cube_translation = cube.getField('translation')

lines = []
with open('Keyframe.txt') as f:
    lines = f.readlines()

coordinates = []

for line in lines:
    if 'Cube' in line:
        coordinates.append(re.findall("\d+\.\d+", line))

count = 0

while supervisor.step(timestep) != -1:
    print(coordinates[count][2])
    
    cube_translation.setSFVec3f([float(coordinates[count][0]), float(coordinates[count][2]), float(coordinates[count][1])])
    
    count += 1
    
    if count >= len(coordinates):
        count = 0
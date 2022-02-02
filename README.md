# Animation To Simulation
This project contains two scripts on python. One is run on the animation software Blender and the other, on the simulation software Webots.

Animation cannot directly be imported into simulation software usually. The aim of this project is to leeway the Keyframe data from Blender. 

Keyframes are created in Blender to manipulate objects and animate them. Coordinate data of the object in scene can be extracted from 
animations using a python script.

Then the scene can be exported to Webots to setup a world. Note that exporting '.blend' files to Webots will require an add-on. This add-on 
only works for until Blender version 2.79 and not yet for the newer versions. Details can be found at: 
https://github.com/cyberbotics/blender-webots-exporter.git

On loading the '.wbt' file in Webots, the Supervisor property has to be checked to 'True' for a robot node. This allows control of the objects 
in the world through a controller script. The script simply translates the defined nodes to the same coordinates as that in the animation 
frames. Later, physics can be activated to check if the animation is a feasible simulation of real-world behaviour.

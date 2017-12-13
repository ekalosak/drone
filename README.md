In silico drone learning environment
-

## Overview
1. Render digital landscape from drone's eye
2. Feed rendered landscape to computer vision module
3. Determine best next command, send to graphics module
4. Repeat

## Progress
Working 3D render of a floor with cubes on it.
Next milestones are:
0. Implement limited movement controls for ML input (u/d, l/r, cw/ccw, fw/bk)
1. Render from multiple viewpoints (e.g. both drone's and bird-eye)
2. Make drone present as rendered object from birds eye
3. Make reinforcement pipeline to teach drone to find a single box in a room
4. Get lighting, blender objects (balls, ropes)

## Getting started
1. Clone the repo `git clone https://github.com/ekalosak/drone.git`
2. Run `python drone_gym.py`

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
1. Render from multiple viewpoints (e.g. both drone's and bird-eye)
2. Implement physics
3. Make reinforcement pipeline to teach drone to hover at height = 1
4. Make reinforcement pipeline to teach drone to find a single box in a room
5. Get textures, lighting, blender objects
6. Render based on what's in line of sight rather than arbitrary obj ordering

## Getting started
1. Clone the repo `git clone https://github.com/ekalosak/drone.git`
2. Run `python drone_gym.py`

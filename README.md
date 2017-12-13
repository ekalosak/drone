In silico drone learning environment
-

## Overview
1. Render digital landscape from drone's eye
2. Feed rendered landscape to computer vision module
3. Determine best next command, send to graphics module
4. Repeat

## Progress
Working 3D render of a cube. Next milestones are:
1. Make simple testing landscape (room with one box)
2. Render from multiple viewpoints (e.g. both drone's and bird-eye)
3. Implement physics
4. Make reinforcement pipeline to teach drone to hover at height = 1
5. Make reinforcement pipeline to teach drone to find a single box in a room
6. Get textures, lighting, blender objects

## Getting started
1. Clone the repo `git clone https://github.com/ekalosak/drone.git`
2. Run `python drone_gym.py`

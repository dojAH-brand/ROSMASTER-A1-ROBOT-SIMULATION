# ROSMASTER A1 — 2D Robot Simulation (Phase 1)

A 2D Ackermann-steered robot simulator built from scratch in Python and pygame.

This is Phase 1 of a longer journey toward building a 3D robot simulation
with ROS 2 and Gazebo, eventually featuring LiDAR and self-navigation.
Before tackling that complexity, I wanted to deeply understand two core
concepts in a simpler environment first: Ackermann steering kinematics
and collision detection — both of which carry directly over into the
3D version.

## Features

- Ackermann steering — identical to a real car
- Collision detection against walls and obstacles
- Live trail visualization showing the path traveled
- Real-time HUD showing speed and position
- Realistic physics — gradual deceleration and self-centering steering when input is released

## Installation

1. Clone the repository
   ```bash
   git clone <your-repo-url>
   cd rosmaster_sim
   ```

2. Create and activate a virtual environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run the simulator
   ```bash
   python3 main.py
   ```

## Controls

| Key | Action |
|-----|--------|
| ↑ Up arrow | Accelerate forward |
| ↓ Down arrow | Reverse |
| ← Left arrow | Steer left |
| → Right arrow | Steer right |
| ESC | Quit the simulator |

## Known limitations

The collision system uses overlap-based detection, meaning it checks
position after movement rather than before — so the robot's edges can
briefly penetrate a wall or obstacle before collision is detected. This
is more noticeable when approaching diagonally, since the current fix
resets both x and y position together rather than per axis. Actively
working on optimizing this.

## Roadmap

- [x] Phase 1 — 2D Ackermann-steered simulator (this repo)
- [ ] Phase 2 — Simulated sensors (LiDAR ray-casting, depth camera)
- [ ] Phase 3 — 3D world rendering
- [ ] Phase 4 — ROS 2 integration
- [ ] Phase 5 — SLAM + autonomous navigation

# ROSMASTER A1 — Phase 3: 3D Robot Simulation

A 3D Ackermann-steered robot simulator built using Panda3D. The 3D model 
dimensions were extracted directly from the official ROSMASTER A1 URDF file 
— every measurement, position and colour reflects the real physical robot.

This is Phase 3 of a longer journey toward building a full ROS 2 simulation 
with LiDAR, SLAM and autonomous navigation.

![ROSMASTER A1 3D](images/Screenshot%20from%202026-07-04%2015-17-22.png)

## Features

- Full 3D model of ROSMASTER A1 — chassis, upper deck, LiDAR mount, 
  depth camera, four blue wheels with grey hubs, fenders and handle bar
- URDF-accurate dimensions — every part built from real robot measurements,
  not guessed or approximated
- Ackermann steering — same physics engine from Phase 1 and 2, now driving 
  a 3D model in real metre units
- Orbit camera — left click and drag to rotate around the robot from any 
  angle, scroll wheel to zoom
- 3D environment — dark ground plane, four grey walls forming a room, 
  two orange obstacles to navigate around
- Panda3D scene graph — parent-child node structure mirrors the URDF 
  link and joint hierarchy directly

## Installation

1. Clone the repository and navigate to the phase3 folder
```bash
   git clone <your-repo-url>
   cd ROSMASTER-A1-ROBOT-SIMULATION/phase3
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

| Key / Input | Action |
|-------------|--------|
| ↑ Up arrow | Accelerate forward |
| ↓ Down arrow | Reverse |
| ← Left arrow | Steer left |
| → Right arrow | Steer right |
| ESC | Quit |
| Left click + drag | Orbit camera around robot |
| Scroll wheel | Zoom in and out |

## Known Limitations

- No 3D collision detection — the robot passes through walls and obstacles.
  Collision detection in 3D requires a physics engine (e.g. Bullet, which 
  is built into Panda3D and will be added in a future update)
- Wheels do not animate or spin as the robot moves
- LiDAR and depth camera sensor visualizations from Phase 2 are not yet 
  connected to the 3D rendering — this comes in Phase 4 with ROS 2

## File Structure

```
phase3/
├── config.py          # all constants from URDF — dimensions, colours
├── main.py            # Panda3D application, game loop, lighting, camera
├── robot3d.py         # 3D robot geometry — make_box, make_cylinder, Robot3D
├── world3d.py         # 3D environment — ground, walls, obstacles
├── robot.py           # Ackermann physics engine (from Phase 1)
├── input_handler3d.py # Panda3D keyboard input handler
├── requirements.txt   # panda3d
├── images/            # screenshots
└── videos/            # demo recordings
```

## Roadmap

- [x] Phase 1 — 2D Ackermann-steered simulator
- [x] Phase 2 — Simulated sensors (LiDAR + depth camera)
- [x] Phase 3 — 3D world rendering with Panda3D
- [ ] Phase 4 — ROS 2 integration
- [ ] Phase 5 — SLAM + autonomous navigation

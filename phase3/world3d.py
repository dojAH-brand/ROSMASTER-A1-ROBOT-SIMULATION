import config
from robot3d import make_box

class World3D:
    def __init__(self, render):

        # ── ground plane ─────────────────────────────────────
        ground = make_box(
            "ground",
            4.0,    # 4 metres wide
            4.0,    # 4 metres long
            0.01,   # very thin — just a flat surface
            (0.15, 0.15, 0.15, 1)   # dark grey
        )
        ground.reparentTo(render)
        ground.setPos(0, 0, -config.WHEEL_RADIUS)

        # ── four walls ───────────────────────────────────────
        wall_thickness = 0.05
        room_size      = 2.0
        wall_height    = 0.3

        walls = [
            # (x,    y,              w,             d,               h)
            (0,             room_size,  room_size*2,  wall_thickness,  wall_height),  # top
            (0,            -room_size,  room_size*2,  wall_thickness,  wall_height),  # bottom
            ( room_size,    0,          wall_thickness, room_size*2,   wall_height),  # right
            (-room_size,    0,          wall_thickness, room_size*2,   wall_height),  # left
        ]

        for x, y, w, d, h in walls:
            wall = make_box(
                "wall",
                w, d, h,
                (0.75, 0.75, 0.75, 1)   # light grey
            )
            wall.reparentTo(render)
            wall.setPos(x, y, -config.WHEEL_RADIUS + h/2)

        # ── two obstacles ────────────────────────────────────
        obstacle1 = make_box("obs1", 0.15, 0.15, 0.2, (1, 0.45, 0.05, 1))
        obstacle1.reparentTo(render)
        obstacle1.setPos(0.8, 0.5, -config.WHEEL_RADIUS + 0.1)

        obstacle2 = make_box("obs2", 0.1, 0.3, 0.2, (1, 0.45, 0.05, 1))
        obstacle2.reparentTo(render)
        obstacle2.setPos(-0.6, -0.4, -config.WHEEL_RADIUS + 0.1)
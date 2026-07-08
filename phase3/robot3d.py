import config
import math

from panda3d.core import (
    GeomVertexFormat, GeomVertexData, GeomVertexWriter,
    Geom, GeomTriangles, GeomNode, NodePath,
    AmbientLight, DirectionalLight,
    LVector4, LPoint3
)



def make_box(name, w, d, h, colour):
    hw = w / 2
    hd = d / 2
    hh = h / 2

    corners = [
        LPoint3(-hw, -hd, -hh),
        LPoint3( hw, -hd, -hh),
        LPoint3( hw,  hd, -hh),
        LPoint3(-hw,  hd, -hh),
        LPoint3(-hw, -hd,  hh),
        LPoint3( hw, -hd,  hh),
        LPoint3( hw,  hd,  hh),
        LPoint3(-hw,  hd,  hh),
    ]

    faces = [
        [0, 1, 2, 0, 2, 3],
        [4, 7, 6, 4, 6, 5],
        [0, 4, 5, 0, 5, 1],
        [2, 6, 7, 2, 7, 3],
        [0, 3, 7, 0, 7, 4],
        [1, 5, 6, 1, 6, 2],
    ]

    fmt   = GeomVertexFormat.getV3c4()
    vdata = GeomVertexData(name, fmt, Geom.UHStatic)
    vdata.setNumRows(36)

    vertex = GeomVertexWriter(vdata, 'vertex')
    color  = GeomVertexWriter(vdata, 'color')
    tris   = GeomTriangles(Geom.UHStatic)

    idx = 0
    for face in faces:
        for vi in face:
            vertex.addData3(corners[vi])
            color.addData4(colour[0], colour[1], colour[2], colour[3])
        tris.addVertices(idx, idx+1, idx+2)
        tris.addVertices(idx+3, idx+4, idx+5)
        idx += 6

    geom = Geom(vdata)
    geom.addPrimitive(tris)
    node = GeomNode(name)
    node.addGeom(geom)
    return NodePath(node)



def make_cylinder(name, radius, length, colour, segments=16):
    fmt   = GeomVertexFormat.getV3c4()
    vdata = GeomVertexData(name, fmt, Geom.UHStatic)

    vertex = GeomVertexWriter(vdata, 'vertex')
    color  = GeomVertexWriter(vdata, 'color')
    tris   = GeomTriangles(Geom.UHStatic)

    half_len = length / 2       

    for i in range(segments):
        angle = 2 * math.pi * i / segments
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        # bottom circle vertex
        vertex.addData3(x, y, -half_len)
        color.addData4(*colour)

        # top circle vertex
        vertex.addData3(x, y, half_len)
        color.addData4(*colour) 
        
    bottom_centre = segments * 2
    vertex.addData3(0, 0, -half_len)
    color.addData4(*colour)

    top_centre = segments * 2 + 1
    vertex.addData3(0, 0, half_len)
    color.addData4(*colour)      
        

    for i in range(segments):
        next_i = (i + 1) % segments

        b0 = i * 2          # current bottom edge point
        t0 = i * 2 + 1      # current top edge point
        b1 = next_i * 2     # next bottom edge point
        t1 = next_i * 2 + 1 # next top edge point

        # side wall — two triangles per segment
        tris.addVertices(b0, b1, t0)
        tris.addVertices(t0, b1, t1)

        # bottom cap — triangle from centre to edge
        tris.addVertices(bottom_centre, b1, b0)

        # top cap — triangle from centre to edge
        tris.addVertices(top_centre, t0, t1)    


    geom = Geom(vdata)
    geom.addPrimitive(tris)
    node = GeomNode(name)
    node.addGeom(geom)
    return NodePath(node)    



class Robot3D:
    def __init__(self, render):
        # create the root node 
        self.root = render.attachNewNode("robot")

        # ── chassis — main body ──────────────────────────────
        chassis = make_box(
            "chassis",
            config.BODY_LENGTH,    # 0.34m long
            config.BODY_WIDTH,     # 0.24m wide
            config.BODY_HEIGHT,    # 0.05m tall
            config.BLACK_COL       # dark black colour
        )
        chassis.reparentTo(self.root)
        chassis.setPos(0, 0, 0)    # centred on root node

        # ── upper deck ───────────────────────────────────────
        upper_deck = make_box(
            "upper_deck",
            0.28, 0.18, 0.02,
            config.DARK_GREY_COL
        )
        upper_deck.reparentTo(self.root)
        upper_deck.setPos(0, 0, 0.03)   

        # ── front bumper ─────────────────────────────────────
        bumper = make_box(
            "bumper",
            0.02, 0.22, 0.04,
            config.BLACK_COL
        )
        bumper.reparentTo(self.root)
        bumper.setPos(0.165, 0, 0)

        # ── LiDAR body ───────────────────────────────────────
        lidar_body = make_box(
            "lidar_body",
            config.LIDAR_BODY_RADIUS * 2,
            config.LIDAR_BODY_RADIUS * 2,
            config.LIDAR_BODY_LENGTH,
            config.DARK_GREY_COL
        )
        lidar_body.reparentTo(self.root)
        lidar_body.setPos(
            config.LIDAR_X,
            config.LIDAR_Y,
            config.LIDAR_Z
        )

        # ── LiDAR orange ring ────────────────────────────────
        lidar_ring = make_box(
            "lidar_ring",
            config.LIDAR_RING_RADIUS * 2,
            config.LIDAR_RING_RADIUS * 2,
            config.LIDAR_RING_LENGTH,
            config.ORANGE_COL
        )
        lidar_ring.reparentTo(self.root)
        lidar_ring.setPos(
            config.LIDAR_X,
            config.LIDAR_Y,
            config.LIDAR_Z + config.LIDAR_RING_Z
        )

        # ── camera body ──────────────────────────────────────
        camera_body = make_box(
            "camera_body",
            config.CAMERA_BODY_LENGTH,
            config.CAMERA_BODY_WIDTH,
            config.CAMERA_BODY_HEIGHT,
            config.LIGHT_GREY_COL
        )
        camera_body.reparentTo(self.root)
        camera_body.setPos(
            config.CAMERA_X,
            config.CAMERA_Y,
            config.CAMERA_Z
        )

        # ── top handle bar ───────────────────────────────────
        handle = make_box(
            "handle",
            0.22, 0.015, 0.03,
            config.LIGHT_GREY_COL
        )
        handle.reparentTo(self.root)
        handle.setPos(0, 0, 0.055)

        # ── logo plate ───────────────────────────────────────
        logo = make_box(
            "logo",
            0.08, 0.001, 0.03,
            config.ORANGE_COL
        )
        logo.reparentTo(self.root)
        logo.setPos(0.17, 0, 0.015)

        # ── four wheels ──────────────────────────────────────
        wheel_positions = [
            ( config.WHEELBASE,  config.TRACK_WIDTH ,  "fl"),
            ( config.WHEELBASE, -config.TRACK_WIDTH ,  "fr"),
            (-config.WHEELBASE,  config.TRACK_WIDTH ,  "rl"),
            (-config.WHEELBASE, -config.TRACK_WIDTH ,  "rr"),
        ]

        for wx, wy, wname in wheel_positions:
            tyre = make_cylinder(
                f"tyre_{wname}",
                config.WHEEL_RADIUS,
                config.WHEEL_WIDTH,
                config.WHEEL_BLUE_COL
            )
            tyre.reparentTo(self.root)
            tyre.setHpr(0, 90, 0)
            tyre.setPos(wx, wy, -config.WHEEL_RADIUS + 0.02)

            hub = make_cylinder(
                f"hub_{wname}",
                0.04,
                config.WHEEL_WIDTH + 0.002,
                config.LIGHT_GREY_COL
            )
            hub.reparentTo(self.root)
            hub.setHpr(0, 90, 0)
            hub.setPos(wx, wy, -config.WHEEL_RADIUS + 0.02)

    def update(self, x, y, heading):
     

        self.root.setPos(x, y, config.WHEEL_RADIUS)

    
        self.root.setH(-math.degrees(heading))





import math
import panda3d
from world3d import World3D
from robot import Robot
from input_handler3d import InputHandler3D
from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, DirectionalLight, LVector4 , ClockObject
from robot3d import Robot3D


class RosmasterSim(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.world3d = World3D(self.render)

        # robot  Ackermann system as Phase 1
        self.robot        = Robot(0, 0)
        self.input_handler = InputHandler3D(self)

        # game loop task 
        self.taskMgr.add(self.game_loop, "game_loop")

        # disable default mouse camera control
        self.disableMouse()

        # position camera to see robot from a good angle
        self.camera.setPos(1, -2, 1)
        self.camera.lookAt(0, 0, 0)

        # set background colour
        self.setBackgroundColor(0.1, 0.1, 0.15, 1)

        # lighting
        ambient = AmbientLight("ambient")
        ambient.setColor(LVector4(0.4, 0.4, 0.4, 1))
        self.render.setLight(self.render.attachNewNode(ambient))

        directional = DirectionalLight("directional")
        directional.setColor(LVector4(0.8, 0.8, 0.8, 1))
        dlight_np = self.render.attachNewNode(directional)
        dlight_np.setHpr(45, -45, 0)
        self.render.setLight(dlight_np)

        
        # create the 3D robot
        self.robot3d = Robot3D(self.render)

        # ── orbit camera setup ───────────────────────────────
        self.camera_distance = 2.0
        self.camera_heading  = 45
        self.camera_pitch    = -20

        self.last_mouse_x = 0
        self.last_mouse_y = 0
        self.mouse_down   = False

        self.accept("mouse1",     self.on_mouse_down)
        self.accept("mouse1-up",  self.on_mouse_up)
        self.taskMgr.add(self.update_camera, "update_camera")
        


    def on_mouse_down(self):
        self.mouse_down = True
        if self.mouseWatcherNode.hasMouse():
            self.last_mouse_x = self.mouseWatcherNode.getMouseX()
            self.last_mouse_y = self.mouseWatcherNode.getMouseY()

    def on_mouse_up(self):
        self.mouse_down = False

    def game_loop(self, task):
        dt = ClockObject.getGlobalClock().getDt()

        # read keyboard and apply to physics robot
        inputs = self.input_handler.get_input()
        self.robot.apply_input(inputs, dt)
        self.robot.update(dt)

        # sync 3D model position with physics position
        self.robot3d.update(self.robot.x, self.robot.y, self.robot.heading)

        return task.cont    

    def update_camera(self, task):
        if self.mouse_down and self.mouseWatcherNode.hasMouse():
            mx = self.mouseWatcherNode.getMouseX()
            my = self.mouseWatcherNode.getMouseY()

            dx = mx - self.last_mouse_x
            dy = my - self.last_mouse_y

            self.camera_heading -= dx * 100
            self.camera_pitch   += dy * 50
            self.camera_pitch    = max(-80, min(-5, self.camera_pitch))

            self.last_mouse_x = mx
            self.last_mouse_y = my

        # position camera based on heading, pitch, distance
        import math
        h_rad = math.radians(self.camera_heading)
        p_rad = math.radians(self.camera_pitch)

        cx = self.camera_distance * math.cos(p_rad) * math.sin(h_rad)
        cy = self.camera_distance * math.cos(p_rad) * math.cos(h_rad)
        cz = self.camera_distance * math.sin(-p_rad)

        self.camera.setPos(cx, -cy, cz)
        self.camera.lookAt(0, 0, 0.05)

        return task.cont    


app = RosmasterSim()
app.run()
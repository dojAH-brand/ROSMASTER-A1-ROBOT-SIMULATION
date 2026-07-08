class InputHandler3D:
    def __init__(self, base):
        self.base = base

    def get_input(self):
        throttle = 0
        steer    = 0

        mw = self.base.mouseWatcherNode

        if mw.is_button_down("arrow_up"):    throttle =  1
        if mw.is_button_down("arrow_down"):  throttle = -1
        if mw.is_button_down("arrow_left"):  steer    = -1
        if mw.is_button_down("arrow_right"): steer    =  1

        return {"throttle": throttle, "steer": steer}
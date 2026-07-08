import config
import pygame
import math

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
      
        self.heading = 0.0
        self.trail = []
        self.trail_timer = 0.0

        self.speed = 0.0
        self.steering_angle = 0.0  


    def update(self, dt):
        steer_rad = math.radians(self.steering_angle)

        if abs(self.steering_angle) > 0.1:
            turning_radius = config.WHEELBASE /math.tan(steer_rad)
            angular_velocity = self.speed / turning_radius
            self.heading += angular_velocity * dt


        self.x += self.speed * math.cos(self.heading) * dt
        self.y += self.speed * math.sin(self.heading) * dt

        self.trail_timer += dt
        if self.trail_timer >= 0.2:
            self.trail.append((self.x, self.y))
            self.trail_timer = 0.0


        self.speed *= config.FRICTION
        self.steering_angle *= config.STEER_RETURN


    def draw(self, screen):

        #for point in self.trail:
            #pygame.draw.circle(screen, config.TRAIL_COL, point, 3)

            
        cos_h = math.cos(self.heading)
        sin_h = math.sin(self.heading)

        hw = config.ROBOT_W /2
        hh = config.ROBOT_H /2

        

        corners = [
            (self.x + cos_h * hw - sin_h *hh,
            self.y + sin_h * hw + cos_h * hh),

            (self.x - cos_h * hw - sin_h *hh,
            self.y - sin_h * hw + cos_h * hh),

            (self.x - cos_h * hw + sin_h *hh,
            self.y - sin_h * hw - cos_h * hh),

            (self.x + cos_h * hw +sin_h *hh,
            self.y + sin_h * hw - cos_h * hh),

        ]

        pygame.draw.polygon(screen, config.ROBOT_COL, corners)

        end_x = self.x + cos_h * (hw + 10)
        end_y = self.y + sin_h * (hw + 10)

        pygame.draw.line(screen, config.HEADING_COL, (self.x, self.y), (end_x, end_y), 3)



    def get_rect(self):
        margin = 4
        pygame.draw.rect
        return pygame.Rect(
            self.x - config.ROBOT_W / 2 + margin,
            self.y - config.ROBOT_H / 2 + margin,
            config.ROBOT_W,
            config.ROBOT_H
        )
    
    
    def apply_input(self, input_dict, dt):
        throttle = input_dict["throttle"]
        steer = input_dict["steer"]

        self.speed += throttle * config.THROTTLE_FORCE * dt

        self.speed = max(-config.MAX_SPEED, min(config.MAX_SPEED, self.speed))

        self.steering_angle += steer * config.MAX_STEER * dt

        self.steering_angle = max(-config.MAX_STEER, min(config.MAX_STEER, self.steering_angle))


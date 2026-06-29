import math
import pygame
import config
import random
import math

class Lidar:
    def __init__(self, num_rays=80, max_range=200, step_size=2):
        self.num_rays = num_rays
        self.max_range = max_range
        self.step_size = step_size
        self.distances = [max_range] * num_rays

    def update(self, robot_x, robot_y, robot_heading, walls):
        angle_step = (2 * math.pi) / self.num_rays
        for i in range(self.num_rays):
           
            angle = robot_heading + i * angle_step
            
            ray_x = robot_x
            ray_y = robot_y
            distance = self.max_range


            for step in range(0, self.max_range, self.step_size):
                ray_x = robot_x + math.cos(angle) * step
                ray_y = robot_y + math.sin(angle) * step

                
                hit = False
                for wall in walls:
                    if wall.collidepoint(ray_x, ray_y):
                        distance = math.sqrt((ray_x - robot_x)**2 + (ray_y - robot_y)**2)

                        hit = True
                        break
                if hit:
                    break    
            
            noise = random.gauss(0, 1.5)
            distance = distance + noise

            distance = max(0 , min(self.max_range, distance))
            self.distances[i] = distance
            

    def draw(self, screen, robot_x, robot_y, robot_heading):
        angle_step = (2 * math.pi) / self.num_rays
        for i in range(self.num_rays):
            angle = robot_heading + i * angle_step
            distance = self.distances[i]

            end_x = robot_x + math.cos(angle) * distance
            end_y = robot_y + math.sin(angle) * distance

            start_offset = (config.ROBOT_W / 2 - 20)  # 30 pixels — half the robot width

            start_x = robot_x + math.cos(angle) * start_offset
            start_y = robot_y + math.sin(angle) * start_offset

            pygame.draw.line(screen,  config.LIDAR_COL, (start_x, start_y), (end_x, end_y), 1)


class DepthCamera():
    def __init__ (self, num_rays= 60, fov=60, max_range=300, step_size=2):
        self.num_rays = num_rays
        self.fov = math.radians(fov)
        self.max_range = max_range
        self.step_size = step_size
        self.distances = [max_range] * num_rays

    def update(self, robot_x, robot_y, robot_heading, walls):
        angle_step =  self.fov/ self.num_rays 
        start_angle = robot_heading - self.fov / 2

        for i in range(self.num_rays):
            angle = start_angle + i * angle_step
            distance = self.max_range

            for step in range(0, self.max_range, self.step_size):
                ray_x = robot_x + math.cos(angle) * step
                ray_y = robot_y + math.sin(angle) * step

                hit = False
                for wall in walls:
                    if wall.collidepoint(ray_x, ray_y):
                        distance = math.sqrt((ray_x - robot_x)**2 + (ray_y - robot_y)**2)

                        hit = True
                        break
                if hit:
                    break    
            self.distances[i] = distance    
   
    def draw(self, screen, robot_x, robot_y, robot_heading):
        angle_step = self.fov / self.num_rays

        for i in range(self.num_rays):
            angle = robot_heading - self.fov / 2 + i * angle_step
            distance = self.distances[i]

            ratio = distance / self. max_range
            red = int(255 * (1 -ratio))
            green = int(255 * ratio)

            colour = (red, green, 0)


            slice_width = config.SCREEN_WIDTH / self.num_rays
            slice_x = i * slice_width


            pygame.draw.rect(screen,  colour, (slice_x, 0, slice_width, 20) )
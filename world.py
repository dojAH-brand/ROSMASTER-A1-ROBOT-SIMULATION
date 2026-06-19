import pygame
import config

class World():
    def __init__(self):
      
      self.screen_walls = [
            pygame.Rect(0, 0, 800, 20),
            pygame.Rect(0, 0, 20, 600),
            pygame.Rect(0, 580, 800, 20),
            pygame.Rect(780, 0, 20, 600),
            pygame.Rect(300, 50, 150, 30),
            pygame.Rect(250, 280, 35, 200),
            ]


    def draw(self, screen):
        for walls in self.screen_walls:
            pygame.draw.rect(screen, config.WALL_COL, walls)

           

    def check_collision(self, robot_rect):
        for wall in self.screen_walls:
            if robot_rect.colliderect(wall):
                return True
            
        return False    

        
import config
import pygame
import sys
from world import World
from robot import Robot
from input_handler import InputHandler


pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption(config.TITLE)
clock = pygame.time.Clock()


world = World()
robot = Robot(400, 300)
input_handler = InputHandler()

pygame.font.init()
font = pygame.font.SysFont("consolas", 18)
running = True

while running:
    
    dt = clock.tick(config.FPS) /1000

   
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

                        
    screen.fill(config.DARK_GREY)

    pre_x , pre_y = robot.x, robot.y

    robot.apply_input(input_handler.get_input() ,dt)
 
    robot.update(dt)

    if world.check_collision(robot.get_rect()):
        robot.x = pre_x
        robot.y = pre_y
        robot.speed = 0

        
    world.draw(screen)
    robot.draw(screen)
 
    pos_text = font.render(f"X {robot.x:.0f}  Y: {robot.y:.0f}", True, config.HUD_COL) 
    speed_text = font.render(f"Speed {robot.speed:.1f}",True, config.HUD_COL)

    screen.blit(pos_text, (27, 30))
    screen.blit(speed_text, (27, 50))

    pygame.display.flip()        

pygame.quit()
sys.exit()    
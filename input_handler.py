import pygame
import config


class InputHandler:
    def __init__(self):
        pass


    def get_input(self):
        keys = pygame.key.get_pressed()

        throttle = 0
        steer = 0

        if keys[pygame.K_UP]:
            throttle = 1

        if keys[pygame.K_DOWN]:
            throttle = -1

        if keys[pygame.K_LEFT]:
            steer = -2

        if keys[pygame.K_RIGHT]:
            steer = 2           

        return {"throttle": throttle,  "steer": steer }    
import pygame
import sys

pygame.init()

# Constants
WIDTH = 1200
HEIGHT = 800
FPS=120
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Variables
key_map = {}
controls = {}

# Classes
class Player:
    def __init__(self,controls,pos=[WIDTH//2,HEIGHT//2],vel=[0,0]):
        self.vel=vel
        self.pos=pos

        self.controls = controls

class Text:
    def __init__(self, text, font, size, color=(255, 255, 255)):
        self.text = text
        self.font = pygame.font.Font(font, size)
        self.color = color
        self.rendered_text = self.font.render(self.text, True, self.color)
        self.rect = self.rendered_text.get_rect()

    def draw(self, surface, pos):
        self.rect.topleft = pos
        surface.blit(self.rendered_text, self.rect)

class Button:
    def __init__(self,pos,size,text='',visible=False):
        pass

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_map[event.key] = True
        elif event.type == pygame.KEYUP:
            key_map[event.key] = False
            print(key_map)

    screen.fill((0, 0, 0))
    pygame.display.flip()

    clock.tick(FPS)
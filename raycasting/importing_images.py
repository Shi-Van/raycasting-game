import pygame
from random import randrange


RES = 700
SIZE = 50
snake_speed = 10
fps = 60
pygame.init()
surface = pygame.display.set_mode([RES, RES])
pygame.display.set_caption('Погоня за хекстеками')
pygame.display.set_icon(pygame.image.load("data\img1.png"))
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 65, bold=True)
img = pygame.image.load("data\img1.png")
img = pygame.transform.scale(img, (50, 50))
img2 = pygame.image.load("data\_cr01mQK8.jpg")
img2 = pygame.transform.scale(img2, (50, 50))
img3 = pygame.image.load("data\img3.png")
img3 = pygame.transform.scale(img3, (40, 40))
img4 = pygame.image.load("data\Visual_Night.jpg")
img4 = pygame.transform.scale(img4, (RES, RES))
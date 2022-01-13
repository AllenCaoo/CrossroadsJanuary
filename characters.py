import pygame
import os
from random import randint

NICOLE = pygame.image.load(os.path.join('src', 'imgs/nicole.jpg'))
ALLEN = pygame.image.load(os.path.join('src', 'imgs/allen.jpg'))
MANDREW = pygame.image.load(os.path.join('src', 'imgs/mandrew.jpg'))
KAITLYN = pygame.image.load(os.path.join('src', 'imgs/kaitlyn.jpg'))
KWANG = pygame.image.load(os.path.join('src', 'imgs/kwang.jpg'))
OLIVER = pygame.image.load(os.path.join('src', 'imgs/oliver.jpg'))
PARK = pygame.image.load(os.path.join('src', 'imgs/park.jpg'))
ZOE = pygame.image.load(os.path.join('src', 'imgs/zoe.jpg'))
ELAINE = pygame.image.load(os.path.join('src', 'imgs/elaine.jpg'))

NICOLE_INJURED = pygame.image.load(os.path.join('src', 'injured/nicole.jpg'))
PARK_INJURED = pygame.image.load(os.path.join('src', 'injured/park.jpg'))
ZOE_INJURED_3 = pygame.image.load(os.path.join('src', 'injured/zoe_3.jpg'))
ZOE_INJURED_2 = pygame.image.load(os.path.join('src', 'injured/zoe_2.jpg'))
ZOE_INJURED_1 = pygame.image.load(os.path.join('src', 'injured/zoe_1.jpg'))
ELAINE_INJURED = pygame.image.load(os.path.join('src', 'injured/elaine.jpg'))

characters = [NICOLE, PARK, ZOE, ELAINE, ALLEN, MANDREW, KAITLYN, KWANG, OLIVER]

characters_injured = [NICOLE_INJURED, PARK_INJURED, ZOE_INJURED_1, ELAINE_INJURED]

zoe_injured = [None, ZOE_INJURED_1, ZOE_INJURED_2, ZOE_INJURED_3]


def get_rand_img_not(id):
    i = randint(0, len(characters) - 1)
    if i == id:
        return get_rand_img_not(id)
    return characters[i]

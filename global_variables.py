import pygame
from pygame.locals import *

"""
	COLOR
"""

GREEN = [50, 168, 82]
GREY = [160, 163, 161]
BLUE = [115, 193, 235]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

#-------------------------------#

"""
	SCREEN
"""

ON = True
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
center_x, center_y = SCREEN_HEIGHT // 2, SCREEN_WIDTH // 2

#-------------------------------#

"""
	VECTOR 2D
"""

init_x = pygame.Vector2(1, 0)
init_y = pygame.Vector2(0, 1)

"""
	VECTOR 3D
"""

init3_x = pygame.Vector3(1, 0, 0)
init3_y = pygame.Vector3(0, 1, 0)
init3_z = pygame.Vector3(0, 0, 1)

"""
	CUBE 3D
"""

verts = [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)]
edges = [(0, 1), (1, 2),(2, 3), (3, 0), (0, 4), (1, 5), (2, 6), (3, 7), (4, 5), (5, 6), (6, 7), (7, 4)]

"""
	PYRAMIDE
"""

verts2 = [(1, 1, -1), (-1, 1, -1), (-1, 1, 1), (1, 1, 1), (0, -1, 0)]
edges2 = [(0, 1),(1,4), (0,4), (1,2), (2, 4), (2, 3), (3, 4), (3, 0)]

"""
	floor
"""

floor_verts = [()]
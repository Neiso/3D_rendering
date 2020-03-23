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
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
center_x, center_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

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

cube_verts = [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)]
cube_edges = [(0, 1), (1, 2),(2, 3), (3, 0), (0, 4), (1, 5), (2, 6), (3, 7), (4, 5), (5, 6), (6, 7), (7, 4)]
cube_faces = [(0, 1, 2, 3)]#, (4, 5, 0, 8)]

"""
	PYRAMIDE
"""

pyramide_verts = [(1, 1, -1), (-1, 1, -1), (-1, 1, 1), (1, 1, 1), (0, -1, 0)]
pyramide_edges = [(0, 1),(1,4), (0,4), (1,2), (2, 4), (2, 3), (3, 4), (3, 0)]

"""
	CUBE 3D + PYRAMIDE ABOVE
"""

cube_pyramide_verts = [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1), (0, -3, 0)]
cube_pyramide_edges = [(0, 1), (1, 2),(2, 3), (3, 0), (0, 4), (1, 5), (2, 6), (3, 7), (4, 5), (5, 6), (6, 7), (7, 4), (0, 8), (1, 8), (4, 8), (5, 8)]

"""
	CUBE 3D + PYRAMIDE ABOVE AND SIDE
"""

cube_pyramide_2_verts = [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1), (0, -3, 0), (0, 3, 0)]
cube_pyramide_2_edges = [(0, 1), (1, 2),(2, 3), (3, 0), (0, 4), (1, 5), (2, 6), (3, 7), (4, 5), (5, 6), (6, 7), (7, 4), (0, 8), (1, 8), (4, 8), (5, 8), (2, 9), (3, 9), (6, 9), (7, 9)]

"""
	SPHERE
"""

sphere_radius = 1
sphere_center = (0, 0, 1)
RAD = 0.0174533


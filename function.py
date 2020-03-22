import pygame
from global_variables import *
pygame.font.init()

font = pygame.font.SysFont("Arial", 18)

def update_fps(clock):
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text

def draw_shape(cube, camera, screen):
	for edge in cube.edges:
		points = []
		for x, y, z in [cube.verts[edge[0]], cube.verts[edge[1]]]:
			x, y = camera.rotate_xy(0.02, x, y)
			x, z = camera.rotate_xz(0.02, x, z)
			y, z = camera.rotate_yz(0.02, y, z)
			x += camera.x
			y += camera.y
			z += camera.z
			
			if z == 0:
				z = 1
			f = 600 / abs(z)
			x, y = int(f*x), int(f*y)
			points += [(center_x + x, center_y + y)]
		pygame.draw.line(screen, WHITE, points[0], points[1], 3)
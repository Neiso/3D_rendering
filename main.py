import pygame
from classes import Camera
from pygame.locals import *
from global_variables import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My first program !")
clock = pygame.time.Clock()

camera = Camera((0, 0, 0))
rad = 0

while (ON):
	dt = clock.tick(60)/1000
	screen.fill(BLACK)

	key = pygame.key.get_pressed()
	camera.update(dt, key)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			ON = False
		elif key[pygame.K_ESCAPE]:
			ON = False

	for edge in edges:
		points = []
		for x, y, z in [verts[edge[0]], verts[edge[1]]]:
			x, y = camera.rotate_xy(rad, x, y)
			x, z = camera.rotate_xz(rad, x, z)
			x += camera.x
			y += camera.y
			z += camera.z
			
			if z == 0:
				z = 1
			f = 600 / z
			x, y = int(f*x), int(f*y)
			points += [(center_x + x, center_y + y)]
		pygame.draw.line(screen, WHITE, points[0], points[1], 3)

	pygame.display.flip()
	rad += 0.0002
	
	print(camera.x, camera.y, camera.z)

pygame.quit()

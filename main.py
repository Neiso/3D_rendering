import pygame
from classes import Camera
from function import *
from pygame.locals import *
from global_variables import *

"	INIT THE PYGAME MODULE	"

pygame.init()

"	INIT THE WINDOW, FULL SCREEN AND PREPARE CLOCK FOR 60 FPS	"

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My first program !")
pygame.display.toggle_fullscreen()
clock = pygame.time.Clock()

"	INIT THE CAMERA (USER's VIEUW) AND SET THE ROTATION		"

camera = Camera((0, 0, 5), (0, 0))
rad = 0

"	MAIN ENGINE		"

while (ON):
	dt = clock.tick(60)/1000
	screen.fill(BLACK)

	key = pygame.key.get_pressed()
	camera.update(0.01, key)
	# camera.rot_yz += 1

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			ON = False
		elif key[pygame.K_ESCAPE]:
			ON = False

	draw_shape(cube_edges, cube_verts, camera, screen)

	screen.blit(update_fps(clock), (10,0))
	pygame.display.flip()
	rad += 0.0002
	
	print(camera.x, camera.y, camera.z)

pygame.quit()

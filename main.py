import pygame
from classes import Camera, Object, Sphere
from function import *
from pygame.locals import *
from global_variables import *

"	INIT THE PYGAME MODULE	"

pygame.init()

"	INIT THE WINDOW, FULL SCREEN AND PREPARE CLOCK FOR 60 FPS	"

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My first program !")
# pygame.display.toggle_fullscreen()
clock = pygame.time.Clock()

"	INIT THE CAMERA (USER's VIEUW) AND SET THE ROTATION		"

camera = Camera((0, 0, -5), (0, 0))

"	MAIN ENGINE		"

cube = Object(cube_verts, cube_edges, cube_faces)
sphere = Sphere(sphere_center, sphere_radius)

while (ON):
	dt = clock.tick(60)/1000
	screen.fill(BLACK)

	key = pygame.key.get_pressed()
	camera.update(0.01, key)
	camera.rot_xy += 1
	camera.rot_xz += 1

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			ON = False
		elif key[pygame.K_ESCAPE]:
			ON = False

	draw_shape(cube, camera, screen)
	render_circle(screen, camera, 600/(1 + abs(camera.z)))


	screen.blit(update_fps(clock), (0,0))
	screen.blit(update_cam_pos(camera), (0, 18))
	pygame.display.flip()
	
	# print(camera.x, camera.y, camera.z)

draw_faces(cube, camera, screen)
pygame.quit()

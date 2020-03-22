import pygame
import math
from global_variables import *
pygame.font.init()

font = pygame.font.SysFont("Arial", 18)

def update_fps(clock):
	fps = "FPS : " + str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text

def update_cam_pos(camera):
	pos = ("X: {0:.3f} Y: {1:.3f} Z: {2:.3f}". format(camera.x, camera.y, camera.z))
	pos_text = font.render(pos, 1, pygame.Color("coral"))
	return pos_text

def draw_shape(object, camera, screen):
	for edge in object.edges:
		points = []
		for x, y, z in [object.verts[edge[0]], object.verts[edge[1]]]:
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

def draw_faces(object, camera, screen):
	color = BLUE
	for face in object.faces:
		points = []
		for edge in [object.edges[face[0]] ,object.edges[face[1]], object.edges[face[2]], object.edges[face[3]]]:
			for x, y, z in [object.verts[edge[0]], object.verts[edge[1]]]:
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
		pygame.draw.polygon(screen, color, points)
		color = GREEN

def render_sphere(screen, camera, sphere):
	x, y, z = sphere.center

	x += camera.x
	y += camera.y
	z += camera.z	
	if z == 0:
		z = 1
	f = 600 / abs(z)
	x, y, radius = int(f*x), int(f*y), int(f*sphere.radius)
	pygame.draw.circle(screen, WHITE, (center_x + x, center_y + y), 2, 2)
	
	angle = RAD
	for i in range(0,270 * 4):
		angle += RAD/3
		x, y = int(math.cos(angle) * f * 1) + center_x, int(math.sin(angle) * f * 1) + center_y
		x, y = camera.rotate_xy(0.02, x, y)
		x += camera.x * f
		y += camera.y * f

		pygame.draw.circle(screen, WHITE, (int(x),int(y)), 0)

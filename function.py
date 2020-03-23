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

def render_sphere(screen, camera, radius):
	# x, y, z = sphere.center

	# x += camera.x
	# y += camera.y
	# z += camera.z	
	# if z == 0:
	# 	z = 1
	# f = 600 / abs(z)
	# x, y = int(f*x), int(f*y)
	# if (abs(x) < 2000 and abs(y) < 2000):
	# 	pygame.draw.circle(screen, WHITE, (center_x + x, center_y + y), 2, 2)
	
	angle = 0
	if radius < 1100:
		nbr_points = int(math.exp(2/math.log(radius)) * 1000)
	else :
		nbr_points = 25000
	angle_val = (math.pi * 2)/nbr_points
	drawn_points = 0
	for i in range(0, nbr_points):
		angle += angle_val
		x, y = int(math.cos(angle) * radius) + center_x, center_y - int(math.sin(angle) * radius)
		x += camera.x * radius
		y += camera.y * radius
		if 0 < x < SCREEN_WIDTH and 0 < y < SCREEN_HEIGHT:
			drawn_points += 1
			pygame.draw.circle(screen, WHITE, (int(x),int(y)), 0)
	print(f"nombre de points dessines: \t{drawn_points}")
	print(f"nombre de points totals:\t{nbr_points}")
	print(f"focal \t\t\t\t{radius}")

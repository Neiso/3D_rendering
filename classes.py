from global_variables import *
import math
import pygame
from pygame.locals import *

class Camera():
	def __init__(self, init_pos=(0, 0, 0), rot=(0,0)):
		self.x = init_pos[0]
		self.y = init_pos[1]
		self.z = init_pos[2]
		self.rot_xy = rot[0]
		self.rot_xz = rot[1]
		self.rot_yz = 0
	
	def rotate_xy(self, dt, x, y):
		x2 = x * math.cos(dt * self.rot_xy) - y * math.sin(dt * self.rot_xy)
		y2 = x * math.sin(dt * self.rot_xy) + y * math.cos(dt * self.rot_xy)
		return (x2, y2)

	def rotate_xz(self, dt, x, z):
		x2 = x * math.cos(dt * self.rot_xz) - z * math.sin(dt * self.rot_xz)
		z2 = x * math.sin(dt * self.rot_xz) + z * math.cos(dt * self.rot_xz)
		return (x2, z2)

	def rotate_yz(self, dt, y, z):
		y2 = y * math.cos(dt * self.rot_yz) - z * math.sin(dt * self.rot_yz)
		z2 = y * math.sin(dt * self.rot_yz) + z * math.cos(dt * self.rot_yz)
		return (y2, z2)

	def update(self, dt, key):
		if key[pygame.K_d]: 	self.x += dt * 2
		if key[pygame.K_q]:		self.x -= dt * 2
		if key[pygame.K_z]:		self.y -= dt * 2
		if key[pygame.K_s]:		self.y += dt * 2
		if key[pygame.K_e]:		self.z -= dt * 2
		if key[pygame.K_a]:		self.z += dt * 2

		if key[pygame.K_o]:		self.rot_xy += 1
		if key[pygame.K_p]:		self.rot_xy -= 1

		if key[pygame.K_l]:		self.rot_xz += 1
		if key[pygame.K_m]:		self.rot_xz -= 1

		if key[pygame.K_b]:		self.rot_yz += 1
		if key[pygame.K_n]:		self.rot_yz -= 1

class Object():
	def __init__(self, verts, edges, faces = []):
		self.verts = verts
		self.edges = edges
		self.faces = faces

class Sphere():
	def __init__(self, center, radius):
		self.center = center
		self.radius= radius
		self.rot_xy = 0
		self.rot_xz = 0
		self.rot_yz = 0

	def rotate_xy(self, dt, x, y):
		x2 = x * math.cos(dt * self.rot_xy) - y * math.sin(dt * self.rot_xy)
		y2 = x * math.sin(dt * self.rot_xy) + y * math.cos(dt * self.rot_xy)
		return (x2, y2)

	def rotate_xz(self, dt, x, z):
		x2 = x * math.cos(dt * self.rot_xz) - z * math.sin(dt * self.rot_xz)
		z2 = x * math.sin(dt * self.rot_xz) + z * math.cos(dt * self.rot_xz)
		return (x2, z2)

	def rotate_yz(self, dt, y, z):
		y2 = y * math.cos(dt * self.rot_yz) - z * math.sin(dt * self.rot_yz)
		z2 = y * math.sin(dt * self.rot_yz) + z * math.cos(dt * self.rot_yz)
# Libraries
import pygame
from sys import exit


# Game setup
resolution = (1920,1080)

pygame.init()
window = pygame.display.set_mode(resolution)
clock = pygame.Clock()


# Surfaces & rectangles
## Ground
placeholder_ground_surface = pygame.Surface((1920,200))
placeholder_ground_surface.fill((255,0,0))
placeholder_ground_rectangle = placeholder_ground_surface.get_rect(topleft = (0,900))

# Player
#player_surface = pygame.image.load()
player_surface = pygame.Surface((100,100))
player_surface.fill((0,255,0))
player_rectangle = player_surface.get_rect(center = (resolution[0]/2,resolution[1]/2))

player_vert_vel = 0
player_vert_acc = 0.3



# Main loop
while True:
	# Event loop
	for event in pygame.event.get():
		# Quit game
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	### DELETE ###
	import time
	if player_rectangle.bottom > placeholder_ground_rectangle.top:
		time.sleep(1)
	### DELETE END ###
	
	# Player physics
	if player_rectangle.bottom < placeholder_ground_rectangle.top:
		player_vert_vel += player_vert_acc
		player_rectangle.y += player_vert_vel
	if player_rectangle.bottom > placeholder_ground_rectangle.top:
		player_rectangle.bottom = placeholder_ground_rectangle.top
		player_vert_vel = 0


	# Render surfaces
	window.fill((0,0,0))
	window.blit(placeholder_ground_surface, placeholder_ground_rectangle)
	window.blit(player_surface, player_rectangle)



	# Update display
	pygame.display.update()

	# Set framerate
	clock.tick(60)

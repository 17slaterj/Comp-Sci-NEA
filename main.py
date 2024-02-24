# Libraries
import pygame
from sys import exit


# Game setup
resolution = (1920,1080)

pygame.init()
window = pygame.display.set_mode(resolution)
pygame.display.set_caption("Cave game") # Placeholder game name
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
player_vert_acc = 0.9

## Controls
move_left = False
move_right = False



# Main loop
while True:
	# Event loop
	for event in pygame.event.get():
		# Key press
		if event.type == pygame.KEYDOWN:
			# Jump
			if event.key == pygame.K_SPACE and player_rectangle.bottom == placeholder_ground_rectangle.top:
				player_vert_vel = -20 
			# Move left
			if event.key == pygame.K_s:
				move_left = True
			# Move right
			if event.key == pygame.K_f:
				move_right = True
		
		# Key release
		if event.type == pygame.KEYUP:
			# Move left
			if event.key == pygame.K_s:
				move_left = False
			if event.key == pygame.K_f:
				move_right = False

		# Quit game
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		
	
	# Player motion
	## Gravity
	player_vert_vel += player_vert_acc
	player_rectangle.y += player_vert_vel
	if player_rectangle.bottom > placeholder_ground_rectangle.top:
		player_rectangle.bottom = placeholder_ground_rectangle.top
		player_vert_vel = 0

	## Movement
	if move_left == True:
		player_rectangle.x -= 5
	if move_right == True:
		player_rectangle.x += 5


	# Render surfaces
	window.fill((0,0,0))
	window.blit(placeholder_ground_surface, placeholder_ground_rectangle)
	window.blit(player_surface, player_rectangle)



	# Update display
	pygame.display.update()

	# Set framerate
	clock.tick(60)

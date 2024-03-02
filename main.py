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
## Sprites
player_idle = pygame.transform.scale(pygame.image.load("Assets\Player\playerIdle.png").convert_alpha(), (256,256))
player_run = (pygame.transform.scale(pygame.image.load("Assets\Player\playerRun1.png").convert_alpha(), (256,256)),
			  pygame.transform.scale(pygame.image.load("Assets\Player\playerRun2.png").convert_alpha(), (256,256)),
			  pygame.transform.scale(pygame.image.load("Assets\Player\playerRun3.png").convert_alpha(), (256,256)),
			  pygame.transform.scale(pygame.image.load("Assets\Player\playerRun4.png").convert_alpha(), (256,256)),
			  pygame.transform.scale(pygame.image.load("Assets\Player\playerRun5.png").convert_alpha(), (256,256)),
			  pygame.transform.scale(pygame.image.load("Assets\Player\playerRun6.png").convert_alpha(), (256,256)),
			  pygame.transform.scale(pygame.image.load("Assets\Player\playerRun7.png").convert_alpha(), (256,256)),
			  pygame.transform.scale(pygame.image.load("Assets\Player\playerRun8.png").convert_alpha(), (256,256)))

## Surface and rectangle
player_surface = player_idle
player_rectangle = player_surface.get_rect(center = (resolution[0]/2,resolution[1]/2))

player_vert_vel = 0
player_vert_acc = 0.9

## Controls
move_left = False
move_right = False

## Animation
run_frame_count = 0
run_sprite_count = 0



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
		
	
	# Player motion and animation
	## Gravity
	player_vert_vel += player_vert_acc
	player_rectangle.y += player_vert_vel
	if player_rectangle.bottom > placeholder_ground_rectangle.top:
		player_rectangle.bottom = placeholder_ground_rectangle.top
		player_vert_vel = 0

	## Movement
	### Left
	if move_left == True:
		# Move left
		player_rectangle.x -= 5

		# Face left
		if run_frame_count == 0:
			player_surface = pygame.transform.flip(player_run[run_sprite_count], True, False)
		run_frame_count += 1
		if run_frame_count == 6:
			run_sprite_count += 1
			run_frame_count = 0
		if run_sprite_count == 8:
			run_sprite_count = 0

	### Right
	if move_right == True:
		# Move right
		player_rectangle.x += 5

		# Face right
		if run_frame_count == 0:
			player_surface = player_run[run_sprite_count]
		run_frame_count += 1
		if run_frame_count == 6:
			run_sprite_count += 1
			run_frame_count = 0
		if run_sprite_count == 8:
			run_sprite_count = 0


	# Render surfaces
	window.fill((0,0,0))
	window.blit(placeholder_ground_surface, placeholder_ground_rectangle)
	window.blit(player_surface, player_rectangle)



	# Update display
	pygame.display.update()

	# Set framerate
	clock.tick(60)

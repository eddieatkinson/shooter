# Duh
# We have access to pygame because we did:
# $ pip install pygame
# It is NOT part of core. This is a 3rd party module.
import pygame

# ---CUSTOM CLASSES HERE---
from Player import Player
# Have to init the pygame object so we can use it.
pygame.init()

# Screen size is a tuple.
screen_size = (1000, 800)
# Because we are going to paint the background, we need a tuple for the color.
background_color = (82, 111, 53) # Plants vs. Zombies green

# Create a screen for pygame to use to draw on.
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("An epic shooter made with python")

the_player = Player('shooter.png', 100, 100, screen)

game_on = True
# Set up the main game loop
while game_on: # Will run forever (until break)
	# Loop through all the pygame events.
	# This is pygame's escape hatch (quit).
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False
		elif event.type == pygame.KEYDOWN:
			if event.key == 273:
				the_player.should_move("up", True)
			elif event.key == 274:
				the_player.should_move("down", True)
			if event.key == 275:
				the_player.should_move("right", True)
			elif event.key == 276:
				the_player.should_move("left", True)
		elif event.type == pygame.KEYUP:
			if event.key == 273:
				the_player.should_move("up", False)
			elif event.key == 274:
				the_player.should_move("down", False)
			if event.key == 275:
				the_player.should_move("right", False)
			elif event.key == 276:
				the_player.should_move("left", False)

	# Paint the screen (no "blit" needed, as it's not an image).
	screen.fill(background_color)
	
	# Must be after fill, or we won't be able to see the hero.
	# screen.blit(the_player_image, [the_player.x, the_player.y])
	the_player.draw_me()

	# Flip the screen, i.e. clear it, so we can draw again...and again...and again
	pygame.display.flip()

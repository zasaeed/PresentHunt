import pygame, sys
from classes import *

lives = 5

#Main Game Function
def runGame(screen):

	#set FPS and Clock variables for ticks
	FPS = 60
	clock = pygame.time.Clock()

	#Set Background image
	background = pygame.image.load('background.jpg')
	screen.blit(background, (0, 0))

	#Load sprites
	present = Present(screen)
	present1 = Present(screen)
	present2 = Present(screen)
	rock = Rock(screen)
	rock2 = Rock(screen)
	player = Player(screen)
	scoreboard = Scoreboard()
	scoreboard.lives = lives

	#Add sprites to corresponding sprite group
	playerSprite = pygame.sprite.Group(player)
	presentSprite = pygame.sprite.Group(present, present1, present2)
	rockSprite = pygame.sprite.Group(rock, rock2)
	scoreboardSprite = pygame.sprite.Group(scoreboard)

	keepGoing = True
	while keepGoing:

		#Check if user presses the exit button
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		#Check for collisions
		collidePresents = pygame.sprite.spritecollide(player, presentSprite, False)
		if collidePresents:
			#If collision occured, increase score by 1
			scoreboard.score += 1
			player.sndPresent.play()
			#Reset present
			for thePresent in collidePresents:
				thePresent.reset()

		#Check for collisions
		collideRocks = pygame.sprite.spritecollide(player, rockSprite, False)
		if collideRocks:
			#If collision occured, decrease life by one
			scoreboard.lives -= 1
			player.sndRock.play()
			#Reset rock
			for theRock in collideRocks:
				theRock.reset()

		if scoreboard.lives <= 0:
			player.sndBackground.stop()
			gameOver(screen, scoreboard)

		#Remove old sprite location image from screen
		playerSprite.clear(screen, background)
		presentSprite.clear(screen, background)
		rockSprite.clear(screen, background)
		scoreboardSprite.clear(screen, background)

		#Update Sprites
		playerSprite.update()
		presentSprite.update()
		rockSprite.update()
		scoreboardSprite.update()

		#Draw Sprites with new data
		playerSprite.draw(screen)
		presentSprite.draw(screen)
		rockSprite.draw(screen)
		scoreboardSprite.draw(screen)

		clock.tick(FPS)

		pygame.display.flip()

def startScreen(screen):

	#Coordinate list for play button
	playButtonCoords = []

	#Set Coordinates
	for x in range(0, 263):
		for y in range(0, 103):
			playButtonCoords.append((385 + x, 294 + y))

	#Coordinate list for instruction button
	instructButtonCoords = []

	#Set Coordinates
	for x in range(0, 261):
		for y in range(0, 101):
			instructButtonCoords.append((389 + x, 445 + y))

	#Set Background
	background = pygame.image.load('startScreen.jpg')
	screen.blit(background, (0, 0))

	pos = (0, 0)

	keepGoing = True
	while keepGoing:

		#Check for events
		for event in pygame.event.get():

			#Check if user presses the exit button
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			#Check when the user presses mouse button
			elif event.type == pygame.MOUSEBUTTONDOWN:
				#Get position when mouse is pressed
				pos = pygame.mouse.get_pos()

		#Check if position is in play button coordinates
		if pos in playButtonCoords:
			setting(screen)

		#Check if position is in instruction button coordinates
		elif pos in instructButtonCoords:
			instructionScreen(screen)

		pygame.display.flip()

def instructionScreen(screen):

	#Set background
	background = pygame.image.load('instructions.jpg')
	screen.blit(background, (0, 0))

	keepGoing = True
	while keepGoing:

		#Check for events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			#Check if user presses any button
			elif event.type == pygame.KEYDOWN:
				setting(screen)

		pygame.display.flip()

def setting(screen):

	#Set background
	background = pygame.image.load('setting.jpg')
	screen.blit(background, (0, 0))

	#Set default choice
	choice = '4'
	#Set lives to a global variable
	global lives

	keepGoing = True
	while keepGoing:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		#Check what key was pressed
		keys = pygame.key.get_pressed()
		#If key pressed was 1
		if keys[pygame.K_1]:
			#Set choice to 1
			choice = '1'
		#If key pressed was 2
		elif keys[pygame.K_2]:
			#Set choice to 2
			choice = '2'
		#If key pressed was 3
		elif keys[pygame.K_3]:
			#Set choice to 3
			choice = '3'


		if choice == '1':
			#Set lives to 2 minutes in miliseconds
			lives = 10
			#Go to runGame
			runGame(screen)

		elif choice == '2':
			#Set lives to 1 minute in miliseconds
			lives = 5
			#Go to runGame
			runGame(screen)

		elif choice == '3':
			#Set lives to 30 seconds in miliseconds
			lives = 1
			#Go to runGame
			runGame(screen)

		pygame.display.flip()

def gameOver(screen, scoreboard):

	#Set background
	background = pygame.image.load('gameOver.jpg')
	screen.blit(background, (0, 0))

	pygame.mixer.init()
	#Set gameover sound
	sndBackground = pygame.mixer.Sound("gameOver.wav")
	sndBackground.play()

	#Get scoreboard
	scoreboardSprite = pygame.sprite.Group(scoreboard)

	keepGoing = True
	while keepGoing:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				#Check if esc key was pressed. If true, exit game.
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
				#Or if the 1 key was pressed. If true, go back to startcreen
				elif event.key == pygame.K_1:
					startScreen(screen)

		#Draw scoreboard
		scoreboardSprite.draw(screen)
		
		pygame.display.flip()
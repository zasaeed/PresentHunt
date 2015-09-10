import pygame
import random

class Player(pygame.sprite.Sprite):
	def __init__(self, screen):
		pygame.sprite.Sprite.__init__(self)
		#set screen
		self.screen = screen
		#Set image
		self.image = pygame.image.load("andy.png")
		#get rectangle around image
		self.rect = self.image.get_rect()

		#set image location
		self.rect.center = (152, 608)

		#X movement speed
		self.dx = 10

		pygame.mixer.init()
		#Set sound for when present is hit
		self.sndPresent = pygame.mixer.Sound("marioCoin.wav")
		#Set sound for when rock is hit
		self.sndRock = pygame.mixer.Sound("rock.wav")
		#Set background music
		self.sndBackground = pygame.mixer.Sound("background.wav")
		#Lower Volume
		self.sndBackground.set_volume(.1)
		# Loop the background music
		self.sndBackground.play(-1)

	def checkKeys(self):
		#Get key pressed
		keys = pygame.key.get_pressed()
		#If key pressed is the left arrow key
		if keys[pygame.K_LEFT]:
			#move image left by x movement speed
			self.rect.centerx -= self.dx
			#Check is image is at the screen border
			if self.rect.centerx < 0:
				#Move to otherside 
				self.rect.centerx = self.screen.get_width()
		elif keys[pygame.K_RIGHT]:
			#more image right by x movement speed
			self.rect.centerx += self.dx
			#Check if image is at the screen border
			if self.rect.centerx > self.screen.get_width():
				#move to otherside
				self.rect.centerx = 0

	def update(self):
		self.checkKeys()

class Present(pygame.sprite.Sprite):
	def __init__(self, screen):
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen
		#set image
		self.image = pygame.image.load("present.png")
		#get rect of image
		self.rect = self.image.get_rect()
		#set falling speed
		self.dy = 5

	def reset(self):
		#set random falling speed
		self.dy = random.randint(4, 10)
		#Move image to top of screen
		self.rect.top = 0
		#Set image at a random horizontal spot on the screen
		self.rect.centerx = random.randrange(0, self.screen.get_width())

	def update(self):
		#Make the image fall
		self.rect.centery += self.dy
		#Check when it reaches the bottom
		if self.rect.top > self.screen.get_height():
			#Reset image
			self.reset()

class Rock(pygame.sprite.Sprite):
	#Same comments as Present Sprite
	def __init__(self, screen):
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen
		self.image = pygame.image.load("rock.png")
		self.rect = self.image.get_rect()

		self.dy = 5

	def reset(self):
		self.dy = random.randint(7, 15)
		self.rect.top = 0
		self.rect.centerx = random.randrange(0, self.screen.get_width())

	def update(self):
		self.rect.centery += self.dy
		if self.rect.top > self.screen.get_height():
			self.reset()

class Scoreboard(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#Set score
		self.score = 0
		#Set lives
		self.lives = 0
		#Set font
		self.font = pygame.font.SysFont("None", 50)

	def update(self):
		#Update text with score and lives
		self.text = "Score: {}   Lives Left: {}".format(self.score, self.lives)
		#Put it on the screen
		self.image = self.font.render(self.text, 5, (0, 0, 0))
		self.rect = self.image.get_rect()
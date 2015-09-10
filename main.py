#Zaid Saeed
#Andy Harris's Present Hunt

#This program is a simple game where the user has to control a character and try to grab
#as many presents as possible.
#The Users are anyone who can press the left and right arrow keys and are bored
#A rock could run this game
#I don't understand the last question

import pygame
from functions import *

pygame.init()

#Set Screen height and width
SCREENHEIGHT = 700
SCREENWIDTH = 700

screen = pygame.display.set_mode((SCREENHEIGHT, SCREENWIDTH))

def main():

	startScreen(screen)

if __name__ == '__main__':
	main()
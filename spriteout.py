# 56x56 sprites
import random, sys, pygame # random is used for the random array generation
# sys is used for the syscall to exit the pygame window
# pygame is used to draw everything, u will probably have to pip install it
# pip install pygame
# on ur command prompt in this directory

# initialize a 1d 56x56 array with all 0s
sprite = [0] * 56 * 56
bf = 10 # bigness factor
buff = 30 # buffer

# this is where u should read in the sprite data
# right now i have a dummy loop creating dummy points
#for i in range(len(sprite)):
#	if random.random() > 0.5:
#		sprite[i] = 1 # this shit kinda makes it look like a qr code ngl


# draws a sprite array to the screen using pygame, results in an infinite draw loop
# 0s output as black, 1s output as white (can be easily changed if u edit the "c" variable for color)
def drawSprite(s):
	pygame.init() # initialize the window
	screen = pygame.display.set_mode([56*bf + 2*buff, 56*bf + 2*buff]) # a surface object to draw to
	
	while 1: # infinite draw loop, passing execution here will stop the rest of ur program
		for event in pygame.event.get(): # leave this alone, receives the signal for the window to close
			if event.type == pygame.QUIT:
				pygame.quit()

		screen.fill((255, 255, 255)) # fill the screen white

		for i in range(len(sprite)):
			# pygame rectangle object (for each point in the sprite): format: (x, y, width, height)
			rect = pygame.Rect(buff + (i*bf)%(56*bf), buff + (i*bf)/56, bf, bf)
			# the 70s being added to the x, y coordinates translate the rectangle to the center
			# the draw function actually puts the sprite into the screen
			if sprite[i] == 0:
				c = 255
			else:
				c = 0
			pygame.draw.rect(screen, [c,c,c], rect) # draw a rect to the surface format: (surface, color tuple, rectangle coordinate object)

		pygame.display.flip() # pushes the screen to be drawn
		# everything you want drawn needs to stay in the infinite draw loop before the flip function is called
		# and after the fill function is called



file = open("pokemon.txt", "rt")
contents = file.read()
file.close()
sprite = contents.split()
print(sprite)


drawSprite(sprite) # call the draw sprite function by passing the sprite array
# sending execution to drawsprite launches the program into an infinite draw loop


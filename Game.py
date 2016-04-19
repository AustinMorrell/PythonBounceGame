import sys, pygame
from astar import *
pygame.init()
pygame.font.init()

def main():

	searchSpace = []
	for x in range(10):
		for y in range(10):
			n = Node(x, y)
			unwalkable = True if (x >= 5 and x <= 6 and y >= 5 and y <= 8) else False
			print("x =:{mx} y=: {my} | pos =: {position}".format(mx = x, my = y, position = n.pos))
			
			n.setWalk(unwalkable)
			searchSpace.append(n)

	size = width, height = 320, 240
	black = 0, 0, 0
	isFull = False
	clock = pygame.time.Clock()

	screen = pygame.display.set_mode(size)

	#-----------------------------------------------------------------------------------
	while 1:
		key = pygame.key.get_pressed()
		if  key[pygame.K_ESCAPE]:
			if isFull == False:
				screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
				isFull = True
			elif isFull == True:
				screen = pygame.display.set_mode(size)
				isFull = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
		
		for i in searchSpace:
			i.draw(screen, (255,0,0))
		
		clock.tick(60)
		screen.fill(black)
		#screen.blit(ball, ballrect)
		pygame.display.flip()
		doit = False
			
main()
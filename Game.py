import sys, pygame
from Sort import *
from astar import *
pygame.init()
pygame.font.init()

def main():

	searchSpace = []
	for x in range(10):
		for y in range(10):
			n = Node(x, y)
			unwalkable = False if (x >= 5 and x <= 6 and y >= 5 and y <= 8) else True
			#print("x =:{mx} y=: {my} | pos =: {position}".format(mx = x, my = y, position = n.pos))
			
			n.setWalk(unwalkable)
			searchSpace.append(n)

	searchSpace[99].WinBox = True
	searchSpace[0].Start = True
	size = width, height = 255, 255
	black = 0, 0, 0
	isFull = False
	clock = pygame.time.Clock()

	screen = pygame.display.set_mode(size)
	Traviler = Astar(searchSpace, searchSpace[0], searchSpace[99], searchSpace[0].pos.x, searchSpace.pos.y)
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
			#screen.fill(black)
			i.draw(screen, (255,255,255))
		
		print(Traviler.pos.x, Traviler.pos.y)
		clock.tick(60)
		#screen.blit(ball, ballrect)
		pygame.display.flip()
		doit = False
			
main()
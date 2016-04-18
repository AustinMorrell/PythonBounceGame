import sys, pygame
pygame.init()
pygame.font.init()

size = width, height = 320, 240
speed = [1,1]
black = 0, 0, 0
doit = True
counter = 0
deltaTime = 0.5
isFull = False

screen = pygame.display.set_mode(size)

ball = pygame.image.load("7C7.gif")
ballrect = ball.get_rect()

while 1:
	key=pygame.key.get_pressed()
	if  key[pygame.K_ESCAPE]:
		if isFull == False:
			screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
			isFull = True
		elif isFull == True:
			screen = pygame.display.set_mode(size)
			isFull = False
	if doit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
		
		ballrect = ballrect.move(speed)
		if ballrect.left < 0 or ballrect.right > width:
			speed[0] = -speed[0]
		if ballrect.top < 0 or ballrect.bottom > height:
			speed[1] = -speed[1]
		
		#screen.fill(black)
		screen.blit(ball, ballrect)
		pygame.display.flip()
		doit = False
	counter += deltaTime
	if counter % 2000 == 0:
		doit = True
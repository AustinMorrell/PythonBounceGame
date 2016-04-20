import pygame as gfx

class Node:
	def __init__(self, x, y):
		self.parent = None
		self.color = (255, 255, 255)
		self.width = 20
		self.height = 20
		self.margin = 5
		self.left = (self.margin + self.width) *  x + self.margin
		self.top = (self.margin + self.height) *  y + self.margin
		self.walkable = True
		self.pos = (x, self.height - y)
		self.f = None
		self.g = None
		self.h = None
		self.image = gfx.image.load("ball.gif")
		self.WinBox = False
		self.Start = False

	def draw(self, screen, color):
		if self.WinBox == False and self.Start == False:
			margin = self.margin
			color = (0, 0, 255) if (self.walkable) else (255,0,0)
			gfx.draw.rect(screen, color, (self.left , self.top, self.width, self.height))
		elif self.WinBox == True:
			margin = self.margin
			color = (0, 255, 0)
			gfx.draw.rect(screen, color, (self.left , self.top, self.width, self.height))
		elif self.Start == True:
			margin = self.margin
			color = (255, 255, 255)
			gfx.draw.rect(screen, color, (self.left , self.top, self.width, self.height))
		
	def setWalk(self, walkable):
		self.walkable = walkable
		 
	def getF(self):
		return self.h + self.g
	def setH(self, val):
		self.h = val
	def setG(self, val):
		self.g = val
		
class Astar:
	def __init__(self, SearchSpace, Start, Goal):
		self.OPEN = []
		self.CLOSED = []
		self.Start = Start
		self.OPEN.append(self.Start)
		self.current = Node(0, 0)
		self.goal = Goal
		self.searchSpace = SearchSpace
	
	def Run(self):
		#self.OPEN.append(self.Start)
		self.current.f = -1
		for a in self.searchSpace:
			if (a.pos[0] == self.current.pos[0] - 1 or a.pos[1] == self.current.pos[1] - 1) and a.walkable == True:
				a.f = 10
				a.parent = self.current
				self.OPEN.append(a)
		while not self.OPEN:
			self.current = self.LowestF(self.OPEN)
	def LowestF(self, Nodes):
		lowestF = -1
		nodeWithLowestF = None
		for node in Nodes:
			if(node.f > lowestF):
				lowestF = node.f
				nodeWithLowestF = node
		return nodeWithLowestF
	
	def Draw(self, screen, color):
		self.left = (5 + 10) *  self.current.pos[0] + 5
		self.top = (5 + 10) *  self.current.pos[1] + 5
		gfx.draw.rect(screen, color, (self.left , self.top, 10, 10))
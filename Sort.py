from operator import itemgetter, attrgetter, methodcaller
from astar import *

def Sort(a_Array):
	for i in range(len(a_Array)):
		for j in range(len(a_Array)-1-i):
			if a_Array[j] > a_Array[j+1]:
				a_Array[j], a_Array[j+1] = a_Array[j+1], a_Array[j]
	
	#for a in a_Array:
		#print(a.pos[0] , a.pos[1])
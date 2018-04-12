import heapq	
import math
class Node:
	def __init__(self):
		#Distance from starting point
		self.g = None
		#Heuristic, prediction
		self.h = None
		self.f = 999

		self.x = None
		self.y = None
		self.parent = None
		self.parent2 = None

	def __lt__(self,other):
		return self.f < other.f

class Maze:
	def __init__(self):
		self.n = int(input("Enter the dimension of the maze"))
		self.nodes = [[] for i in range(self.n)]
		for i in range(self.n):
			for j in range(self.n):
				temp = Node()
				temp.x = i
				temp.y = j
				self.nodes[i].append(temp)

	def take_input(self):
		line = input("Enter the blocked space")
		while line:
			line = line.split()
			self.nodes[int(line[0])][int(line[1])] = -1
			line = input()
		line = input("Enter start and end co-ordinates")
		line = line.split()
		self.find_path(int(line[0]),int(line[1]),int(line[2]),int(line[3]))

	def find_path(self,startx,starty,endx,endy):
		opened = []
		opened2 = []
		closed2 = []
		closed = []
		start = self.nodes[startx][starty]
		start2 = self.nodes[endx][endy]
		start2.parent = start2
		start.parent = start
		start.g = 0
		start2.g = 0
		start2.f = 0
		start.f = 0
		opened.append(start)
		opened2.append(start2)
		while(len(opened) > 0 and len(opened2) > 0):	
			#O(n)
			heapq.heapify(opened)
			heapq.heapify(opened2)
			q = heapq.heappop(opened)
			q2 = heapq.heappop(opened2)
			if(q == q2):
				print("Path Found!")
				print("Path is:")
				print(q.x,q.y)
				a = q.parent
				b = q.parent2

				while(a.parent!=a and b.parent != b):
					print(a.x,a.y,"      ",b.x,b.y)
					a = a.parent
					b = b.parent		
				print(a.x,a.y,"      ",b.x,b.y)							
				return
			neighbours = self.get_neighbours(q)
			neighbours2 = self.get_neighbours(q2)			
			for neighbour in neighbours:
				if neighbour.parent == None:
					neighbour.parent = q
				prevf = neighbour.f					
				neighbour.g = q.g + 1
				#Euclidean Distance
				neighbour.h = math.sqrt((neighbour.x - endx)** 2+(neighbour.y - endy)** 2)
				neighbour.f = neighbour.g + neighbour.h

				if neighbour in opened or neighbour in closed:
					if neighbour.f < prevf:
						opened.append(neighbour)

					else:
						neighbour.f = prevf
				else:
					opened.append(neighbour)
			closed.append(q)

			for neighbour2 in neighbours2:
				if neighbour2.parent == None:
					neighbour2.parent = q2
				else:
					neighbour2.parent2 = q2
				prevf = neighbour2.f					
				neighbour2.g = q2.g + 1
				#Euclidean Distance
				neighbour2.h = math.sqrt((neighbour2.x - startx)** 2 +(neighbour2.y - starty)** 2)
				neighbour2.f = neighbour2.g + neighbour2.h

				if neighbour2 in opened2 or neighbour2 in closed2:
					if neighbour2.f < prevf:
						opened2.append(neighbour2)
					else:
						neighbour2.f = prevf
				else:
					opened2.append(neighbour2)
			closed2.append(q2)
		print("No path found!")

	def get_neighbours(self,a):
		temp = []
		x = a.x
		y = a.y
		add(self,x + 1,y - 1,temp,self.n)
		add(self,x,y - 1,temp,self.n)
		add(self,x - 1,y - 1,temp,self.n)
		add(self,x - 1,y,temp,self.n)
		add(self,x - 1,y + 1,temp,self.n)
		add(self,x,y + 1,temp,self.n)
		add(self,x + 1,y,temp,self.n)
		add(self,x + 1,y + 1,temp,self.n)
		return temp

def add(self,x,y,list,n):
	if x > -1 and x < n and y > -1 and y < n and self.nodes[x][y] != -1:
		list.append(self.nodes[x][y])

M = Maze()
M.take_input()
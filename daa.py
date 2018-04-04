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
		closed = []
		start = self.nodes[startx][starty]
		start.parent = start
		start.g = 0
		start.f = 0
		opened.append(start)
		while(len(opened) > 0):	
			#O(n)
			heapq.heapify(opened)
			q = heapq.heappop(opened)
			neighbours = self.get_neighbours(q)
			for neighbour in neighbours:
				if neighbour.parent == None:
					neighbour.parent = q
				if neighbour.x == endx and neighbour.y == endy:
					print("Path found!")
					print("Path is: ")
					while(neighbour.parent != neighbour):
						print(neighbour.x,neighbour.y)
						neighbour = neighbour.parent
					print(neighbour.x,neighbour.y)

					return
				else:

					prevf = neighbour.f					
					neighbour.g = q.g + 1
					#Euclidean Distance
					neighbour.h = math.sqrt(abs((neighbour.x - endx)* 2 +(neighbour.y - endy)* 2))
					neighbour.f = neighbour.g + neighbour.h

					if neighbour in opened or neighbour in closed:
						if neighbour.f < prevf:
							opened.append(neighbour)

						else:
							neighbour.f = prevf
					else:
						opened.append(neighbour)
			closed.append(q)

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
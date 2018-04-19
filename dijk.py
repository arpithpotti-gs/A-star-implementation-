import heapq	
import math
import time
class Node:
	def __init__(self):
		#Distance from starting point
		self.g = None
		self.symbol = None
		self.x = None
		self.y = None
		self.parent = None
		self.parent2 = None

	def __lt__(self,other):
		return self.g < other.g

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
		for i in range(self.n):
			line = input()
			for j in range(len(line)):
				self.nodes[i][j].symbol = line[j]
				if line[j] == 'S':
					startx = i
					starty = j
				elif line[j] == 'E':
					endx = i
					endy = j
		self.find_path(startx,starty,endx,endy)
	def find_path(self,startx,starty,endx,endy):
		starttime = time.time()
		self.path_length = 0
		self.test = 0
		opened = []
		opened2 = []
		closed2 = []
		closed = []
		start = self.nodes[startx][starty]
		start.parent = start
		start2 = self.nodes[endx][endy]
		start2.parent = start2
		start.g = 0
		start2.g = 0
		opened.append(start)
		opened2.append(start2)
		while(len(opened) > 0 and len(opened2) > 0):
			self.test = self.test + 1	
			#O(n)
			heapq.heapify(opened)
			heapq.heapify(opened2)
			q = heapq.heappop(opened)
			q2 = heapq.heappop(opened2)

			if(q.symbol != 'S' or q2.symbol != 'E'):
				q.symbol = '*'
				q2.symbol = '-'
			neighbours = self.get_neighbours(q,1)
			neighbours2 = self.get_neighbours(q2,2)
		
			for neighbour in neighbours:
				prevg = neighbour.g					
				neighbour.g = q.g + 1
				if neighbour.parent == None:
					neighbour.parent = q
				else:
					neighbour.parent2 = q
				if neighbour.symbol == '-':
					endtime = time.time()
					x = neighbour
					y = q.parent
					q.symbol = '%'
					while(x.parent!= x):
						self.path_length = self.path_length + 1
						x.symbol = '%'
						x = x.parent
					while(y.parent!= y):
						self.path_length = self.path_length + 1
						y.symbol = '%'
						y = y.parent
					print("Path found!")
					print("Searched space is:")
					for i in range(self.n):
						for j in range(self.n):
							print(self.nodes[i][j].symbol,end = "")
						print()	
					print("Time taken is :",endtime - starttime)
					print("Length of the shortest path is",self.path_length + 1)	
					return
				if neighbour in opened or neighbour in closed:
					if neighbour.g < prevg:
						opened.append(neighbour)
					else:
						neighbour.g = prevg
				else:
					opened.append(neighbour)
			closed.append(q)

			for neighbour2 in neighbours2:
				prevg = neighbour2.g					
				neighbour2.g = q2.g + 1

				if neighbour2.parent == None:
					neighbour2.parent = q2
				else:
					neighbour2.parent2 = q2
				if neighbour2.symbol == '*':
					endtime = time.time()
					print("Path         found")
					x = neighbour2
					y = q2.parent2
					q2.symbol = '%'
					while(x.parent!= x):
						self.path_length = self.path_length + 1
						x.symbol = '%'
						x = x.parent
					while(y.parent!= y):
						self.path_length = self.path_length + 1
						y.symbol = '%'
						y = y.parent					
					print("Searched Space is:")
					for i in range(self.n):
						for j in range(self.n):
							print(self.nodes[i][j].symbol,end = "")
						print()	
					print("Time taken is :",endtime - starttime)	
					print("Length of the shortest path is",self.path_length + 1)
					print(self.test)

					return
				if neighbour2 in opened2 or neighbour2 in closed2:
					if neighbour2.g < prevg:
						opened2.append(neighbour2)
					else:
						neighbour2.g = prevg
				else:
					opened2.append(neighbour2)
			closed2.append(q2)
		print("No path found!")

	def get_neighbours(self,a,flag):
		temp = []
		x = a.x
		y = a.y
		if flag == 1:
			add(self,x + 1,y - 1,temp,self.n)
			add(self,x,y - 1,temp,self.n)
			add(self,x - 1,y - 1,temp,self.n)
			add(self,x - 1,y,temp,self.n)
			add(self,x - 1,y + 1,temp,self.n)
			add(self,x,y + 1,temp,self.n)
			add(self,x + 1,y,temp,self.n)
			add(self,x + 1,y + 1,temp,self.n)
			return temp
		else:
			add2(self,x + 1,y - 1,temp,self.n)
			add2(self,x,y - 1,temp,self.n)
			add2(self,x - 1,y - 1,temp,self.n)
			add2(self,x - 1,y,temp,self.n)
			add2(self,x - 1,y + 1,temp,self.n)
			add2(self,x,y + 1,temp,self.n)
			add2(self,x + 1,y,temp,self.n)
			add2(self,x + 1,y + 1,temp,self.n)
			return temp

def add(self,x,y,list,n):
	if x > -1 and x < n and y > -1 and y < n and self.nodes[x][y].symbol != '#'and self.nodes[x][y].symbol != 'S'and self.nodes[x][y].symbol != 'E'and self.nodes[x][y].symbol != '*':
		list.append(self.nodes[x][y])
def add2(self,x,y,list,n):
	if x > -1 and x < n and y > -1 and y < n and self.nodes[x][y].symbol != '#'and self.nodes[x][y].symbol != 'S'and self.nodes[x][y].symbol != 'E'and self.nodes[x][y].symbol != '-':
		list.append(self.nodes[x][y])

M = Maze()
M.take_input()
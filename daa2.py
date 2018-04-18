import heapq	
import math
import time
class MinHeap(object):
	def __init__(self,n):
		self.array = []
		self.size = n
	def getLeft(self,i):
		return self.array[2*i].dist
	def getRight(self,i):
		return self.array[2*i+1].dist

	def heapify(self,i):
		if self.check(i):
			return
		else:
			if 2*i <= self.size:
				max=2*i
				if 2*i+1 <= self.size:
					if self.getRight(i) < self.getLeft(i):
						max=2*i+1
			else:
				if 2*i+1 <= self.size:
					max=2*i+1
				else:
					return
			temp = self.array[max]
			self.array[max] = self.array[i]
			self.array[i] = temp
		if (2*max <= self.size) or (2*max+1 <= self.size):		
			self.heapify(max)
	def check(self,i):
		if 2*i <= self.size:
			if (self.getLeft(i) < self.array[i].dist):
				return False
		if 2*i+1 <= self.size:
			if (self.getRight(i) < self.array[i].dist):
				return False
		return True
	def buildHeap(self):
		for i in range(self.size,0,-1):
			self.heapify(i)
	def extractMin(self):
		if self.size >= 1:
			temp=self.array[0]
			self.array[0]=self.array[self.size]
			self.size -= 1
			self.heapify(1)
			return temp
		else:
			print("empty heap")
	def updatePriority(self,v):
		for i in range(1,self.size+2):
			if self.array[i] == v:
				break
		parent= i//2
		if  not self.check(parent):
			temp = self.array[i]
			self.array[i] = self.array[parent]
			self.array[parent] = temp
		if parent//2 > 1:
			self.updatePriority(self.array[parent//2])

class Node:
	def __init__(self):
		#Distance from starting point
		self.dist = 999
		#Heuristic, prediction
		self.symbol = None
		self.x = None
		self.y = None

class Maze:
	def __init__(self):
		self.n = int(input("Enter the dimension of the maze"))
		self.Q = []
		self.H = MinHeap(self.n)
		self.nodes = [[] for i in range(self.n)]
		self.take_input()

	def take_input(self):
		for i in range(self.n):
			for j in range(self.n):
				temp = Node()
				temp.x = i
				temp.y = j
				self.nodes[i].append(temp)
				self.H.array.append(temp)
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
		start = self.nodes[startx][starty]
		start.dist = 0
		self.H.buildHeap()
		self.H.heapify(1)
		for i in self.H.array:
			print(i.symbol,i.dist)
		while(self.H.size != 0):
			x = self.H.extractMin()
			# print(x.dist)	
			neighbours = self.get_neighbours(x)
			for neighbour in neighbours:
				if neighbour.symbol == 'E':
					endtime = time.time()
					print("Path Found")
					print("Path is:")
					for i in range(self.n):
						for j in range(self.n):
							print(self.nodes[i][j].symbol,end = "")
						print()				
					return	
				if neighbour.dist > x.dist + 1:
					# print("Hi")
					neighbour.dist = x.dist + 1
					a = neighbour.x
					b = neighbour.y
					self.nodes[a][b].symbol = '*'
					self.H.updatePriority(neighbour)
		print("Path not Found!")
		for i in range(self.n):
			for j in range(self.n):
				print(self.nodes[i][j].symbol,end = "")
			print()
			
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
	if x > -1 and x < n and y > -1 and y < n and self.nodes[x][y].symbol != '#' and self.nodes[x][y].symbol != 'S' and self.nodes[x][y].symbol != 'E' and self.nodes[x][y].symbol != '*':
		list.append(self.nodes[x][y])

M = Maze()
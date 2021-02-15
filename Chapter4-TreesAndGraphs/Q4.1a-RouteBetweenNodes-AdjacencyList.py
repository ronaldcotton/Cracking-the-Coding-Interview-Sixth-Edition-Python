#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Adjacency List

# Q4.1 - Route Between Nodes

class AdjacencyList:
	def __init__(self, numOfNodes=None):
		if numOfNodes is not None and numOfNodes > 0:
			self.matrix = [[] for _ in range(numOfNodes)]
			self.numOfNodes = numOfNodes
			self.matrixVisited = []
			self.searchReturnValue = None
			self.path = ""
			self.searchFor = None
		
	# [1:-1] is a python trick to remove brackets from a list
	def __str__(self):
		returnStr = ""
		for index, result in enumerate(self.matrix):
			returnStr+=str(index) + ": " + str(result)[1:-1] + "\n"
		return returnStr
		
	def add(self, Node=None, directedEdgeTo=None):
		if Node == None or directedEdgeTo == None:
			return None
		else:
			try:
				self.matrix[Node].append(directedEdgeTo)
			except IndexError:
				return None 

	# need the recursed parameter to set the values of 
	# self.matrixVisited to the number of Nodes available.
	def depthFirstSearch(self, searchValue, node=0, recursed=False):
		if recursed == False:
			self.matrixVisited = [False] * self.numOfNodes
			self.searchReturnValue = None
			self.searchFor = searchValue
		if node == self.searchFor:
			self.searchReturnValue = node
			return self.searchReturnValue
		if len(self.matrix) == 0 or self.matrixVisited == True:
			return self.searchReturnValue
		self.matrixVisited[node] = True
		for m in self.matrix[node]:
			if m == self.searchFor:
				self.searchReturnValue = m
			if self.matrixVisited[m] == False:
				self.depthFirstSearch(searchValue, m, True)
		return self.searchReturnValue

	def depthFirstSearchPath(self, searchValue, node=0, recursed=False):
		if recursed == False:
			self.matrixVisited = [False] * self.numOfNodes
			self.searchReturnValue = None
			self.searchFor = searchValue
			self.path = str(node)
		if node == self.searchFor:
			self.searchReturnValue = node
			return self.path
		if len(self.matrix) == 0 or self.matrixVisited == True:
			return self.searchReturnValue
		self.matrixVisited[node] = True
		self.path += " -> "
		for m in self.matrix[node]:
			if m == self.searchFor:
				self.searchReturnValue = m
			if self.matrixVisited[m] == False:
				self.path += str(m)
				self.depthFirstSearchPath(searchValue, m, True)
		if self.path[-1:] != ' ': # return if complete path
			return self.path

		
	def breadthFirstSearch(self, searchValue, node=0):
		# searchValue can never be greater than number of Nodes
		# or less than 0
		if searchValue > self.numOfNodes or searchValue < 0:
			return None
		# this can find values in multiple graphs
		for i in range(self.numOfNodes):
			for m in self.matrix[i]:
				if m == searchValue:
					return m
		# because searchValue == Node number - solution is trivial and
		# should never reach this next line
		return None
			
	
# See graphs on page 106 and number list on middle of page
# Cracking the Coding Interview, 6th Edition

if __name__ == "__main__":
	
	Lst = AdjacencyList(7)
	Lst.add(0,1)
	Lst.add(1,2)
	Lst.add(2,0)
	Lst.add(2,3)
	Lst.add(3,2)
	Lst.add(4,6)
	Lst.add(5,4)
	Lst.add(6,5)
	print(Lst)
	# First variable for depthFirstSearchPath is the node to search for
	# second variable is for the root node to search from
	# There's two directed graphs in the node
	print("depthFirstSearchPath(5,4): " + str(Lst.depthFirstSearchPath(5,4)))
	print("depthFirstSearchPath(3): " + str(Lst.depthFirstSearchPath(3)))
	print("self.path: " + str(Lst.path))





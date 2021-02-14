#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Adjacency List

# Adjacency is 
class AdjacencyList:
	def __init__(self, numOfNodes=1):
		self.Matrix = [[] for _ in range(numOfNodes)]
	
	# [1:-1] is a python trick to remove brackets
	def __str__(self):
		returnStr = ""
		for index, result in enumerate(self.Matrix):
			returnStr+=str(index) + ": " + str(result)[1:-1] + "\n"
		return returnStr
		
	def add(self, Node=None, directedEdgeTo=None):
		if Node == None or directedEdgeTo == None:
			return None
		else:
			try:
				self.Matrix[Node].append(directedEdgeTo)
			except IndexError:
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

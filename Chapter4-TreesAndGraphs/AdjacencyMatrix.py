#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Adjacency Matricies

# True means contains Adjacency, False Means it does not.
class AdjacencyMatrix:
	def __init__(self, sizex=1, sizey=1):
		self.matrix = [[] for _ in range(sizey)]
		for x in range(sizex):
			for y in range(sizey):
				self.matrix[y].append(False)
	
	def __str__(self):
		return str(self.matrix)
		
	def add(self, Node=None, directedEdgeTo=None):
		if Node == None or directedEdgeTo == None:
			return None
		else:
			try:
				self.matrix[Node][directedEdgeTo] = True
			except IndexError:
				return None 
	
# TODO - Depth First Search and Breadth First Search

# See top of page 107 of Cracking the Coding Interview, 6th Edition
if __name__ == "__main__":
	Mat = AdjacencyMatrix(4,4)
	Mat.add(0,1)
	Mat.add(1,2)
	Mat.add(2,0)
	Mat.add(3,2)
	print(Mat)

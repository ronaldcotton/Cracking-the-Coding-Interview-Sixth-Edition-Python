#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Binary Search Tree

# Attempting to follow PEP8 convention when naming:
# https://www.python.org/dev/peps/pep-0008/
# https://realpython.com/python-pep8/
# TODO - fix all other code - follow this convention. 

class BinaryNode:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def __str__(self):
		if self.data is not None:
			return str(data) # IDK best way to implement printing only a node
		return ""

	# TODO rewrite getters and setters as Python Property:
	# https://docs.python.org/3/library/functions.html#property
	def get_data(self):
		return self.data
	
	def set_data(self, data=None):
		self.data = data
		
	def get_left(self):
		return self.left
	
	def set_left(self, left=None):
		self.left = left

	def get_right(self):
		return self.right
	
	def set_right(self, right=None):
		self.right = right

	def insert(self, data=None):
		if data is None or self.data == data:
			return None # TODO data already in BST, return with error would be best
		elif self.data < data:
			if self.left is not None:
				return self.left.insert(data)
			else:
				self.left = BinaryNode(data)
				return data
		else: # self.data > data
			if self.right is not None:
				return self.right.insert(data)
			else:
				self.right = BinaryNode(data)
				return data
			
	def is_empty(self):
		return self.value == self.left == self.right == None

	def inorder_tranversal(self):
		if self.data is not None:
			if self.left is not None:
				return self.left.inorder_traversal()
			if self.data is not None:
				return self.data + " "
			if self.node.right is not None:
				return inorder_traversal(self.node.right)

	def preorder_transversal(self):
		pass # TODO

def postorder_transversal(self):
		pass # TODO

class BST:
	def __init__(self, root=None):
		self.root = root
	
	def __str__(self):
		pass # TODO
		
	def set_root(self, root=None):
		self.root = root
	
	def get_root(self):
		return self.root

if __name__ == "__main__":
	root = BinaryNode(1)
	root.insert(2)
	root.insert(3)
	root.insert(4)
	root.insert(5)
	print(root.inorder_tranversal())
	

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Binary Search Tree

class BinaryNode:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def __str__(self):
		if self.data is not None:
			return str(self.data)
		return ""

	def insert(self, data=None):
		if data is None or self.data == data:
			return None 
		elif self.data > data:
			if self.left is not None:
				return self.left.insert(data)
			else:
				self.left = BinaryNode(data)
				return data
		else: # self.data < data
			if self.right is not None:
				return self.right.insert(data)
			else:
				self.right = BinaryNode(data)
				return data
			
	def is_empty(self):
		return self.value == self.left == self.right == None

	def inorder_traversal(self):
		if self.data is not None:
			if self.left is not None:
				self.left.inorder_traversal()
			if self.data is not None:
				print(str(self.data), end=' ')
			if self.right is not None:
				self.right.inorder_traversal()
	
	def preorder_traversal(self):
		if self.data is not None:
			if self.data is not None:
				print(str(self.data), end=' ')
			if self.left is not None:
				self.left.preorder_traversal()
			if self.right is not None:
				self.right.preorder_traversal()
	
	def postorder_traversal(self):
		if self.data is not None:
			if self.left is not None:
				self.left.postorder_traversal()
			if self.right is not None:
				self.right.postorder_traversal()
			if self.data is not None:
				print(str(self.data), end=' ')

# adapted from - https://stackoverflow.com/a/62856494
def sidewaysTree(node, level=0, last=None):
	if node != None:
		sidewaysTree(node.left, level + 1, True)
		if level==0:
			print(node.data)
		else:
			char = '\\'
			if last == True:
				char = '/'
			print(' ' * 4 * level + char, node.data)
		sidewaysTree(node.right, level + 1, False)
 
 
if __name__ == "__main__":
	root = BinaryNode(3)
	root.insert(2)
	root.insert(1)
	root.insert(5)
	root.insert(4)
	print('inorder (ascending order): ', end='')
	root.inorder_traversal()
	print('\npreorder (root is first node visited): ', end='')
	root.preorder_traversal()
	print('\npostorder (root is last node visited): ', end='')
	root.postorder_traversal()
	print('\nsideways tree (left leafs of tree at top of page):')
	print('|lvl'*10) # seperates each level of tree
	sidewaysTree(root)
	

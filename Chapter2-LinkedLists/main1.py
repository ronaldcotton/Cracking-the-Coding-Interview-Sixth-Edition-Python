#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Setup -- Singly LinkedList
# Python Example

class Node(object):
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next
	
	def __repr__(self):
		if self.data is not None:
			return self.data
		return "None"
		
class LinkedList(object):
	def __init__(self, head=None):
		self.head = head
		
	def __repl__(self):
		return self.head

	def __str__(self):
		node = self.head
		output = ""
		while node is not None:
			output += str(node.data) + ' -> '
			node = node.next
		output += 'None'
		return output

if __name__ == "__main__":
	ll = LinkedList() # create Linked List
	ll.head = Node('first node, head of linked list')
	ll.head.next = Node('second node')
	(ll.head.next).next = Node('third node, tail of linked list')
	print(ll)

	print(Node('fourth node - not in linked list'))
	print(Node()) # Last Node with nothing in it




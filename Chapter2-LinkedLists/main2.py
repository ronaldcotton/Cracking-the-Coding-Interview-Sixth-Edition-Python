#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Setup -- Singly LinkedList
# Deleting a Node from a Singly LinkedList
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

	# remove_node removes first element that matches data
	# returns 1 if element was deleted, returns 0 otherwise
	def remove_node(self, data):
		if data is None:
			return
		node = self.head
		last = None
		while node is not None:
			if node.data == data:
				if node == self.head: # if node is the head
					self.head = node.next
					node = None # memory deallocation - Node = None or "del node" deallocates
					del node 
					return 1
				else: # if node is not head
					last.next = node.next
					node = None  # memory deallocation - Node = None or "del node" deallocates
					del node
					return 1
			last = node
			node = node.next
		return 0
					
if __name__ == '__main__':
	ll = LinkedList() # create Linked List
	ll.head = Node('first node, head of linked list')
	ll.head.next = Node('second node')
	(ll.head.next).next = Node('third node, tail of linked list')
	print(ll)

	print('Delete Middle Node:')
	ll.remove_node('second node')
	print(ll)

	print('Delete Node That Doesn\'t Exist:')
	ll.remove_node('no such node')
	print(ll)

	print('Delete Last Node:')
	ll.remove_node('third node, tail of linked list')
	print(ll)

	print('Delete Head Node:')
	ll.remove_node('first node, head of linked list')
	print(ll)
	

	

	

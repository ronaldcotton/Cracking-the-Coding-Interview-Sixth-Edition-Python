#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Setup -- Singly LinkedList
# Deleting a Node from a Singly LinkedList
# plus Interview Question 2.1 - Remove Duplicates from Linked List
# plus Interview Question 2.2 - kth from Last Element
# plus Interview Question 2.3 - delete middle node - given only node
# plus Interview Question 3.4 - Partition
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
	
	# remove_dup1 - remove duplicates, not using extra memory
	def remove_dup1(self):
		node = self.head
		move = node.next
		last = node
		while node is not None:
			while move is not None:
				if node.data == move.data:
					last.next = move.next
					move = None # dealloc
					move = last.next
				else:
					move = move.next
					last = last.next
			last = node = node.next
			if last is not None:
				move = last.next
			
	
	# remove_dup2 - remove duplicates, using extra memory
	def remove_dup2(self):
		last = node = self.head
		move = node.next
		moved = False
		check_list = []
		check_list.append(last.data)
		while move is not None:
			for check in check_list:
				if check == move.data:
					last.next = move.next
					move = None
					move = last.next
					moved = True
					break
			if moved is not True:
				move = move.next
				last = last.next
				check_list.append(last.data)
			else:
				moved = False
	
	def kthfromtheend(self, k): # iterative - can also be done with recursion
			move = node = self.head
			count = 1
			for i in range(k):
				if move is not None:
					move = move.next
				else:
					return None
			while move is not None:
				node = node.next
				move = move.next
			return node.data
	
	def delete_middle_node(self, node):
		move = self.head  # never the first or last node
		while (move.next).next != node.next:
			if move is not None:
				move = move.next
			else:
				return None
		move.next = (move.next).next
		node = None

	def partition(self, partition):
		move = self.head
		print(move.data + " " + move.next.data + " " + move.next.next.data)
		list_less_than = list_equal_greater = None
		list_lt = list_eg = None
		while move is not None:
			if int(move.data) < partition:
				print( move.data + " <")
				if list_less_than is None:
					list_lt = list_less_than = move
					list_lt.next = list_less_than.next = None
				else:
					if list_less_than.next is None:
						list_lt.next = list_less_than.next = move
					else:
						list_lt.next = move
			else: # node.data =< partition
				print("=<")
				if list_equal_greater is None:
					list_eg = list_equal_greater = move
					list_eg.next = list_equal_greater.next = None
				else:
					if list_equal_greater.next is None:
						list_eg.next = list_equal_greater.next = move
					else:
						list_eg.next = move
						
			move = move.next
			print(move.data)
		
		list_eg.next = None
		list_lt.next = list_equal_greater
		self.head = list_less_than
	
if __name__ == '__main__':
	ll = LinkedList() # create Linked List
	ll.head = Node('1')
	ll.head.next = Node('2')
	(ll.head.next).next = Node('3')
	((ll.head.next).next).next = Node('4')
	(((ll.head.next).next).next).next = Node('5')
	print("Linked List:")
	print(ll)
	
	ll.partition(3)
	
	print("Linked List - After Partition:")
	print(ll)
	


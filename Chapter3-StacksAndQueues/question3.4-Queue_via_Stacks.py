#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 3.4 Queue via Stacks
# Using Two Stacks - Implement a Queue

class Stack:
    def __init__(self):
        self.stack = []
    
    def __str__(self):
        return str(self.stack)

    # --- stack commands - LIFO ---
    # remove last element from array
    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
    
    def push(self, value):
        return self.stack.append(value)
    
    def peek(self):
        len_stack = len(self.stack)
        if len_stack != 0:
            return self.stack[len_stack-1]

    def isEmpty(self):
        return len(self.stack) == 0

class Queue:
	def __init__(self):
		self.queue = Stack()
		
	def __str__(self):
		return str(self.queue)

	def add(self, value):
		return self.queue.push(value)
		
	def remove(self):
		temp = Stack()
		# pop everything off the first stack, place into temp
		# better implementation can be made later
		while not self.queue.isEmpty():
			temp.push(self.queue.pop())
		# remove one element - keep to return at end of method
		ret = temp.pop()
		# place things back into original queue
		while not temp.isEmpty():
			self.queue.push(temp.pop())
		return ret
		
	# TODO not optimized - needs to be revisisted
	def seek(self):
		temp = Stack()
		while not self.queue.isEmpty():
			temp.push(self.queue.pop())
		ret = temp.peek()
		while not temp.isEmpty():
			self.queue.push(temp.pop())
		return ret

if __name__ == "__main__":
    s = Stack()

    # testing stack
    print(s.isEmpty())
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)
    print(s.pop())
    print(s.peek())
    print(s)

    q = Queue()
    # testing queue
    # print(q.isEmpty())
    q.add(1)
    q.add(2)
    q.add(3)
    print(q)
    print(q.remove())
    print(q.seek())
    print(q)

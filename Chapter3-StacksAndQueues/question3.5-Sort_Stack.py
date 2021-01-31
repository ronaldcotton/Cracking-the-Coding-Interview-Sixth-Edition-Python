#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 3.5 - Sort Stack

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

def sort(stack):
	temp_stack = Stack()
	
	if stack.isEmpty():
		return temp_stack

	temp2_stack = Stack()

	temp_stack.push(stack.pop())
	
	while not stack.isEmpty():	
		if temp_stack.peek() < stack.peek():
			temp_stack.push(stack.pop())
		else:
			while not temp_stack.isEmpty() and temp_stack.peek() > stack.peek():
				temp2_stack.push(temp_stack.pop())
			temp_stack.push(stack.pop())
			while not temp2_stack.isEmpty():
				temp_stack.push(temp2_stack.pop())

	return temp_stack 

if __name__ == "__main__":
    s = Stack()

    # testing stack
    print(s.isEmpty())
    s.push(2)
    s.push(20)
    s.push(15)
    s.push(111)
    s.push(1)
    print(s)
    s = sort(s)
    print(s)
    print(s.pop())
    print(s.peek())
    print(s)



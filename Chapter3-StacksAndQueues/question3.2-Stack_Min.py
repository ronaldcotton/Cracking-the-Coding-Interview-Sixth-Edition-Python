#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 3.2 - Stack Min
# if Stack min is required to be 0(1) time, but you are allowed to both
# push() and pop() elements in the stack, you need an additional list for the min

class Stack:
    def __init__(self):
        self.stack = []
        self.min_list = []
    
    def __str__(self):
        return str(self.stack)

    # --- stack commands - LIFO ---
    # remove last element from array
    def pop(self):
        if len(self.stack) != 0:
            pop_value = self.stack[len(self.stack)-1]
            self.min_list.remove(pop_value)
            return self.stack.pop()
    
    def push(self, value):
        self.min_list.append(value)
        self.min_list.sort() # need to place value in correct location if not empty or min
        return self.stack.append(value)
    
    def peek(self):
        len_stack = len(self.stack)
        if len_stack != 0:
            return self.stack[len_stack-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def min(self):
        if len(self.min_list) > 0:
            return self.min_list[0]
    
    def print_min_list(self):
        print("min_list: " + str(self.min_list))

if __name__ == "__main__":
    s = Stack()
    print(s.push(3))
    print(s.push(2))
    print(s.push(1))
    print(s.push(-1))
    print(s.push(-5))
    print(s.push(100))
    print(s.push(7))
    print(s.push(8))
    for i in range(8):   
        print("stack: " + str(s))
        s.print_min_list()
        print("min in stack: " + str(s.min()))
        print("popping off end of stack: " + str(s.pop()))

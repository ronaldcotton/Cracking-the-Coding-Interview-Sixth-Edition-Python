#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 3.3
# Stack of Plates
# thres

from random import random

class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = 5
    
    def __str__(self):
        return str(self.stack)

    # --- stack commands - LIFO ---
    # remove last element from array
    def pop(self):
        if len(self.stack) != 0:
            pop_value = self.stack[len(self.stack)-1]
            return self.stack.pop()
    
    def push(self, value):
        if len(self.stack) < self.max_stack:
            return self.stack.append(value)
        else:
            return None
    
    def peek(self):
        len_stack = len(self.stack)
        if len_stack != 0:
            return self.stack[len_stack-1]

    def isEmpty(self):
        return len(self.stack) == 0
    
    def isFull(self):
        return len(self.stack) == self.max_stack

def rando(value):
    return round(random()*value)

class SetOfStacks:
    def __init__(self):
        self.set = []
        self.set.append(Stack())
        self.stack_index = 0

    def __str__(self):
        s = ""
        for r in range(self.stack_index+1):
            s+=str(self.set[r])+'\n'
        s+="---"
        return s

    def add(self, value):
        if self.set[self.stack_index].isFull():
            self.set.append(Stack())
            self.stack_index+=1
        self.set[self.stack_index].push(value)
    
    def remove(self):
        if self.set[self.stack_index].isEmpty():
            self.set.pop()
            self.stack_index-=1
        self.set[self.stack_index].pop()

if __name__ == "__main__":
    s = SetOfStacks()
    print("add:")
    for r in range(21):
        s.add(rando(1000))
        print(s)
    print("remove:")
    for r in range(10):
        s.remove()
        print(s)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class StackQueue:
    def __init__(self):
        self.stackqueue = []
    
    def __str__(self):
        return str(self.stackqueue)

    # --- stack commands - LIFO ---
    # remove last element from array
    def pop(self):
        if len(self.stackqueue) != 0:
            return self.stackqueue.pop()
    
    def push(self, value):
        return self.stackqueue.append(value)
    
    def peek(self):
        len_stackqueue = len(self.stackqueue)
        if len_stackqueue != 0:
            return self.stackqueue[len_stackqueue-1]

    def isEmpty(self):
        return len(self.stackqueue) == 0
    
    # --- queue commands - FIFO ---
    def add(self, value):
        return self.stackqueue.append(value)

    # remove first element from array
    def remove(self):
        if len(self.stackqueue) != 0:
            return self.stackqueue.pop(0)
    
    def seek(self):
        if len(self.stackqueue) != 0:
            return self.stackqueue[0]

if __name__ == "__main__":
    s = StackQueue()

    # testing stack
    print(s.isEmpty())
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)
    print(s.pop())
    print(s.peek())
    print(s)

    q = StackQueue()
    # testing queue
    print(q.isEmpty())
    q.add(1)
    q.add(2)
    q.add(3)
    print(q)
    print(q.remove())
    print(q.seek())
    print(q)
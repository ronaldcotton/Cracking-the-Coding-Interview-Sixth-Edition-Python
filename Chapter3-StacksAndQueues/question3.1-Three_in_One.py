#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 3.1 - Three in One

class StackQueue:
    def __init__(self):
        self.number_of_splits = 3
        self.stackqueue = []
        self.start = [0 for x in range(self.number_of_splits)]
        self.end = [0 for x in range(self.number_of_splits)]
    
    def __str__(self):
        return_str = ""
        for s in range(self.number_of_splits):
            return_str += "\nQueueStack #" + str(s) + ": " + str(self.stackqueue[self.start[s]:self.end[s]])
        return return_str
    # all commands below assume that -1 < emement < self.number_of_splits

    # for debugging
    def print_array(self):
        print(str(self.stackqueue))
        for i in range(self.number_of_splits):
            print(str(i) + "- elements " + str(self.start[i]) + " - " + (str(self.end[i])))

    # --- stackqueue commands - LIFO ---
    # remove last element from array
    def pop(self, element):
        if self.start[element] != self.end[element]:
            self.end[element]-=1
            for i in range(element+1, self.number_of_splits):
                self.start[i]-=1
                self.end[i]-=1
            return self.stackqueue.pop(self.end[element])
    
    def push(self, element, value):
        self.stackqueue.insert(self.end[element], value)
        self.end[element]+=1
        for i in range(element+1, self.number_of_splits):
            self.start[i]+=1
            self.end[i]+=1
        return value
 
    def peek(self, element):
        if self.start[element] != self.end[element]:
            return self.stackqueue[self.end[element]]

    def isEmpty(self, element):
        return self.start[element] == self.end[element]
    
    # --- queue commands - FIFO ---
    def add(self, element, value):
        self.stackqueue.insert(self.end[element], value)
        self.end[element]+=1
        for i in range(element+1, self.number_of_splits):
            self.start[i]+=1
            self.end[i]+=1
        return value

    # remove first element from array
    def remove(self, element):
        if self.start[element] != self.end[element]:
            self.end[element]-=1
            for i in range(element+1, self.number_of_splits):
                self.start[i]-=1
                self.end[i]-=1
            return self.stackqueue.pop(self.start[element])
    

    # "seek" for queue similiar to "peek" for stack    
    def seek(self, element):
        if self.start[element] != self.end[element]:
            return self.stackqueue[self.start[element]]

if __name__ == "__main__":
    s = StackQueue()
    print(s)
    print(s.isEmpty(0))
    print(s.isEmpty(1))
    print(s.isEmpty(2))

    s.push(0, 1)
    s.push(0, 2)
    s.push(0, 3)

    s.push(1, 11)
    s.push(1, 12)
    s.push(1, 13)

    s.push(2, 21)
    s.push(2, 22)
    s.push(2, 23)

    print(s)
    s.print_array()
    print(s.pop(0))
    print(s.pop(0))
    print(s.pop(0))
    print(s.pop(0)) # returns None becuase no elements of the stack to pop
    print(s.pop(1))
    print(s.pop(1))
    print(s.pop(2))
    print(s)

    q = StackQueue()
    print(q)

    q.add(0, 1)
    q.add(0, 2)
    q.add(0, 3)

    q.add(1, 11)
    q.add(1, 12)
    q.add(1, 13)

    q.add(2, 21)
    q.add(2, 22)
    q.add(2, 23)

    print(q)
    print(q.remove(0))
    print(q.remove(0))
    print(q.remove(0))
    print(q.remove(0))
    print(q.remove(1))
    print(q.remove(1))
    print(q.remove(2))
    print(q.seek(0))
    print(q)

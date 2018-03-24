# -*- coding: utf-8 -*-

"""
Q
Describe a queue data structure that is implemented using one or more stacks.

Don't worry about running time.  Write the enqueue and dequeue operations for the  queue.  You may use any language you like.

BCR : O(1)
Time Complexity :
insert : O(1)
dequeue : O(2N)
space : O(2N)
"""

#FIFO ;
class Stack(object):
    def __init__(self):
        self.array = []
    def enqueue(self, value):
        self.array.insert(0, value) #at the very beginning
    def dequeue(self):
        #when you print, material inside already executed
        return(self.array.pop())
    def isempty(self):
        return(self.array == [])
    def show(self):
        print(self.array)




#Queue using Stacks...
#every time dequeue, bring to another queue, then do...

class Queue(object):
    def __init__(self):
        self.stack = Stack() #wow, Stack can work w/"object"
    def push(self, value):
        self.stack.enqueue(value)
    def pop(self):
        s = Stack()
        while not self.stack.isempty():
            s.enqueue(self.stack.dequeue())
        buff = s.dequeue() #this should print.
        while not s.isempty():
            v = s.dequeue()
            self.stack.enqueue(v)
        return buff
    def show(self):
        self.stack.show()

s = Queue()
s.push(3)
s.push(4)
s.push(2)
s.push(5)
s.push(1)
s.show()
s.pop()
s.show()

"""
disclaimer :
if "show" in Queue is also necessary, insert would not be O(1).
"""

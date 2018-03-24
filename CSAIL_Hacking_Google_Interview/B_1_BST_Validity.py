# -*- coding: utf-8 -*-

import sys

"""
Q
Write a function to determine whether a given binary tree of distinct integers is a  valid binary search tree.  Assume that each node contains a pointer to its left child, a  pointer to its right child, and an integer, but not a pointer to its parent.  You may use  any language you like.
"""
#FIFO
class Queue(object):
    def __init__(self):
        self.list = []
    def enqueue(self, value):
        self.list.insert(0, value)
    def dequeue(self):
        return(self.list.pop()) #does this return?
    def isempty(self):
        return self.list==[]


class Node(object):
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

class BST(object):
    def __init__(self):
        self.root = None
    def add(self, value):
        if self.root == None:
            self.root = Node(value, None, None)
        else:
            current = self.root
            while (1):
                if value<current.value:
                    if current.left == None:
                        current.left = Node(value, None, None)
                        break
                    current = current.left
                else:
                    if current.right==None:
                        current.right = Node(value, None, None)
                        break
                    current = current.right
    def add_false(self, value):
        if self.root == None:
            self.root = Node(value, None, None)
        else:
            current = self.root
            while (1):
                if value>current.value:
                    if current.left == None:
                        current.left = Node(value, None, None)
                        break
                    current = current.left
                else:
                    if current.right==None:
                        current.right = Node(value, None, None)
                        break
                    current = current.right
    def DFS(self, current):
        if current == None:
            return
        print("%s -> " %(current.value)),
        if current.left !=  None:
            self.DFS(current.left)
        if current.right != None:
            self.DFS(current.right)

    def BFS(self, current, q):
        if current == None:
            return
        print("%s -> " %(current.value)), #no None, I guess
        if current.left != None:
            q.enqueue(current.left)
        if current.right != None:
            q.enqueue(current.right)
        if q.isempty():
            return
        now = q.dequeue()
        self.BFS(now, q)
    def isbst(self, current):
        if current == None:
            return
        print("%s -> " %(current.value)),
        if current.left !=  None:
            #print("(left is %s)" %current.left.value),
            if current.value >= current.left.value:
                return "False! False alert!"
            self.isbst(current.left)
        if current.right != None:
            #print("(right is %s)" %current.right.value),
            if current.value < current.right.value:
                return "False! False alert!"
            self.isbst(current.right)
        return True


t = BST()
t.add(15)
t.add(8)
t.add(20)
t.add(1)
t.add(12)
t.add(15)
t.add(40)
t.add(0)
t.add(4)
t.add(2)
t.add(16)

t.DFS(t.root)
print("\n")

q = Queue()
t.BFS(t.root, q)
print("\n")
print(t.isbst(t.root))

f = BST()
f.add_false(15)
f.add_false(8)
f.add_false(20)
f.add_false(1)
f.add_false(12)
f.add_false(15)
f.add_false(40)
f.add_false(0)
f.add_false(4)
f.add_false(2)
f.add_false(16)
print("\n")
print(f.isbst(f.root))


#check valid; BFS or DFS?

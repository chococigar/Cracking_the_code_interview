# -*- coding: utf-8 -*-

"""
Write a function to remove a single occurrence of an integer from a doubly linked  list if it is present.  You may use any language you like.
"""

class Node(object):
     def __init__(self, data, left_child, right_child): #initdata?
        self.name = ""
        self.data = data
        self.left_child = left_child #no parent?! zero or more child nodes.
        self.right_child = right_child
    #midway realized insert, delete, etc can be in Node instead.

#Binary search tree;
#BST : All left are less than right descendents.
class BST(object):
    def __init__(self):
        self.root = None #declare a new node as root.
    def append(self, data):
        if self.root == None: #no root; first of tree.
            self.root = Node(data, None, None)
        else: #need to tell parents that I'm children...
            current = self.root
            while True:#not a root
                if data>=current.data: #break before going to children.
                    if current.right_child != None:
                        current = current.right_child
                    else:
                        current.right_child = Node(data, None, None)
                        break
                else:
                    if current.left_child != None: #break before child.
                        current = current.left_child
                    else:
                        current.left_child = Node(data, None, None)
                        break
    def search_bool(self, data):
        current = self.root
        while current.data != data:#not a root
            print(current.data)
            if data>=current.data: #break before going to children.
                if current.right_child != None:
                    current = current.right_child
                else: #child is None.
                    return False
            else:
                if current.left_child != None: #break before child.
                    current = current.left_child
                else: #child is None.
                    return False
        return True
    def remove(self, data): #return None or tree removed.
        current = self.root
        while current.data != data:#not a root
            print(current.data)
            if data>=current.data: #break before going to children.
                if current.right_child != None:
                    current = current.right_child
                else: #child is None.
                    print("Not here")
                    return #reached end
            else:
                if current.left_child != None: #break before child.
                    current = current.left_child
                else: #child is None.
                    print("Not here")
                    return #reached end
        if (current.left_child == None and current.right_child==None):
            current = None
            print("no child")
        elif (current.left_child != None and current.right_child != None): #both are not empty.
            sub = current.left_child.max()
            self.remove(sub)
            current = sub
            print("two children")
            # current is Node; you want a tree. I guess starting from that node...
            #time complexity for starting from that node?
        elif (current.left_child != None):
            current = current.left_child
            print("left child")
        elif (current.right_child!=None):
            current = current.right_child
            print("right child")


    def max(self):#current is not None.
        current = self.root
        while current.right_child != None:
            current = current.right_child
        return current

bst = BST()
bst.append(15)
bst.append(6)
bst.append(20)
bst.append(18)
bst.append(24)
bst.append(1)
bst.append(8)
bst.append(3)
bst.append(16)
bst.append(19)
bst.append(22)
bst.append(25)
bst.append(21)
#print(bst.search_bool(4))
#print(bst.search_bool(49))
bst.remove(24)

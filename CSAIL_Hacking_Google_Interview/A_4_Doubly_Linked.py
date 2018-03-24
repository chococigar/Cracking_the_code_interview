# -*- coding: utf-8 -*-

"""
Write a function to remove a single occurrence of an integer from a doubly linked  list if it is present.  You may use any language you like.
Time Complexity : delete, add, all O(n)
"""

class Node(object):
    def __init__(self, value, prev, next):
        self.self = self
        self.value = value
        self.prev = prev
        self.next = next


class Doubly_Linked(object): #doublylinked tree.
    def __init__(self):
        self.root = None
    def add(self, value): #at end.
        if self.root==None: #was empty.
            self.root = Node(value, None, None)
        else:
            current = self.root
            while current.next != None:
                current = current.next
            current.next = Node(value, None, None)
            current.next.prev = current
        return None
    def delete(self, value):
        if self.root==None: #separate case for when only one?
            return None
        else:
            current = self.root
            while current.next != None:
                if current.next.value == value:
                    if current.next.next==None:
                        current.next = None
                    else:
                        current.next = current.next.next
                        current.next.prev = current
                    return None
                current = current.next
            print("Not found~")
            return None
    def delete2(self, value): #wow what a beautiful code.
        current = self.root
        while current != None:
            if current.value == value: #first? last?
                if current.prev != None: #if not first.
                    current.prev.next = current.next
                if current.next != None:
                    current.next.prev = current.prev #What about "None's prev?"
                return None
            current = current.next
        print("Not found ~('-')~")
        return None

    def show(self):
        if self.root == None:
            print("~('-')~")
        else:
            current=self.root
            while current.next != None:
                print("%s -> " %current.value),
                current = current.next
            print(current.value)

d = Doubly_Linked()
d.add(5)
d.add(24)
d.add(14141)
d.add(3)
d.add(24)
d.add(14141)
d.add(3)
d.add(24)
d.show()
d.delete2(3)
d.show()
d.delete2(4545)
d.show()

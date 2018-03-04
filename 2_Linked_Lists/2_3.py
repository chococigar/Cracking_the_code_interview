"""
Delete a node in the middle of a singly list, given only access to that node.
Implemented in the code.
"""


class Node(object):
    def __init__(self, data, next): #initdata?
        self.data = data
        self.next = next

class SinglyList(object):

    head = None
    tail = None

    def show(self): #1 argument = self
        print("Showing all the nodes")
        current = self.head
        while current != None:
            print current.data, "->",
            current = current.next

    def append(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
        self.tail = node

    def remove(self, node_value):
        current = self.head
        previous = None
        while current != None:
            if current.data == node_value:
                if previous == None: #no need to set tail if last node?
                    self.head = current.next

                else:
                    previous.next = current.next

            previous = current
            current = current.next



s = SinglyList()
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(5)
s.remove(2)
s.show()

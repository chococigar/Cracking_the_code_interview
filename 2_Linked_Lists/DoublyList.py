class Node(object):
    def __init__(self, data, prev, next): #initdata?
        self.data = data
        self.prev = prev
        self.next = next

class DoublyList(object):
    head = None
    tail = None

    def show(self):
        print("Printing all linked list elements")
        current = self.head
        while current != None:
            print current.data, "->",
            current = current.next

    def append(self, data):
        node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            #node.next = None; already init.
            self.tail.next = node
            self.tail = node

    def remove(self, node_value):
        current = self.head
        while current != None:
            if current.data == node_value:
                if current.prev == None:
                    self.head = current.next
                    current.next.prev = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
            current = current.next

d = DoublyList()
d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.append(5)
d.append(2)
d.append(3)
d.append(4)
d.append(5)
d.show()
d.remove(1)
d.remove(2)
d.show()

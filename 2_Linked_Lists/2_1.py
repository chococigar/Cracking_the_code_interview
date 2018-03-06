"""
Remove duplicates from an unsorted linked list.
(2. Const : if temporary buffer is not allowed?)
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
        print("")

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

#average time complexity for python dict is O(1); worst case O(n), similar to hash table. (dict is generic name)
    def remove_duplicate(self):
        dic = {}
        current = self.head
        while current!= None:
            if current.data in dic:
                self.remove(current.data) #not just node, but data.
            dic[current.data] = "1"
            current = current.next
        self.show()
        return(self)

    #no buffer allowed; has O(n^2) time, but O(1) space.
    def remove_duplicate2(self):
        current = self.head
        while current != None:
            runner = current
            while runner.next != None:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
        return(self)



s = SinglyList()
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(3)
s.append(4)
s.append(5)
s.show()
s.remove_duplicate2()
s.show()

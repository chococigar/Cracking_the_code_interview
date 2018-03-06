class Node(object):
    def __init__(self, data, next): #initdata?
        self.data = data
        self.next = next

class SinglyList(object):

    head = None
    tail = None

    def show(self): #1 argument = self
        print("\nShowing all the nodes")
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

    def link2num(self):
        current = self.head
        s = ''
        while current != None:
            s = ''.join([s, str(current.data)])
            current = current.next
        return int(s)



def list2linked(listy):
    s = SinglyList()
    for elem in listy:
        s.append(elem)
    return(s)



f = open("2_5_input.txt", 'r') #also, input is automatically taken as string.
left, right = f.readline().strip().split(" + ")
left = list2linked([int(x) for x in left[1:-1].split(" -> ")])#initial input condition
right = list2linked([int(x) for x in right[1:-1].split(" -> ")])#initial input condition

list2linked([int(c) for c in str(int(str(left.link2num())[::-1]) + int(str(right.link2num())[::-1]))[::-1]]).show()

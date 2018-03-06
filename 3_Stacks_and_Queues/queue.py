#alternative method : use lists as stack
class Queue :
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return (self.items==[])
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        self.items.pop() #first in first out. last item is first.
    def size(self):
        return len(self.items)
    def show(self):
        print("top "),
        for elem in self.items:
            print elem, ", ",
        print("bottom (first out)")

s = Queue()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.enqueue(4)
s.enqueue(5)
s.show()

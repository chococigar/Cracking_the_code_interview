#alternative method : use lists as stack
#this still worked without "object". why?
class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return (self.items==[])
    def push(self, item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def peek(self):
        return(self.items[-1])
    def size(self):
        return len(self.items)
    def show(self):
        print("bottom "),
        for elem in self.items:
            print elem, ", ",
        print("top")

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.show()

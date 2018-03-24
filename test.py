# -*- coding: utf-8 -*-

print(hash(1))
print(hash(2))
print(hash(3))
print(hash(4))
print(hash(5))
print(hash("a"))
print(hash("b"))
print(hash("c"))
print(hash("d"))
print(hash("e"))

class string(object):
    def __hash__(self):
        if not self:
            return 0 # empty
        value = ord(self[0]) << 7
        for char in self:
            value = c_mul(1000003, value) ^ ord(char)
        value = value ^ len(self)
        if value == -1:
            value = -2
        return value

s = string()

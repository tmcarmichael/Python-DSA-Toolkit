# Implement a Stack (LIFO) that supports: push(), pop(), peek(), isEmpty(), and size() methods.

class Stack(object):
  def __init__(self, items=[]):
    self.items = items

  def isEmpty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    self.items.pop()

  def peek(self):
    return self.items[len(self.items)-1]

  def size(self):
    return len(self.items)

# Usage: 

s = Stack()
s.isEmpty()
s.push(1)
s.push(2)
s.push(3)
s.peek()
s.size()
s.isEmpty()
s.pop()
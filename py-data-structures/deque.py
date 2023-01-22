# Implement a Deque that supports: pop(), popleft(), append(), appendleft(), isEmpty(), and size() methods.

class Deque(object):
  def __init__(self, items=[]):
    self.items = items

  def isEmpty(self):
    return self.items == []

  def appendleft(self, item):
    self.items.insert(0, item)

  def append(self, item):
    self.items.append(item)

  def popleft(self):
    return self.items.pop(0)

  def pop(self):
    return self.items.pop()

  def size(self):
    return len(self.items)

# Usage:

d = Deque()
d.isEmpty()
d.append(1)
d.append(2)
d.appendleft(3)
d.size()
d.popleft()
d.pop()
d.size()
d.isEmpty()
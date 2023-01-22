# Implement a Queue (FIFO) that supports: enqueue(), dequeue(), isEmpty(), and size() methods.

class Queue(object):
  def __init__(self, items=[]):
    self.items = items

  def isEmpty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.insert(0, item)

  def dequeue(self):
    return self.items.pop()

  def size(self):
    return len(self.items)

# Usage:

q = Queue()
q.size()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
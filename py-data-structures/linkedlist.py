# Implement a Linked List that supports: insert(), insertAtEnd(), printList()

# List Node class
class Node:
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insert()
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  # printList()
  def printList(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next

# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()
# Implement a Linked List that supports: push_front(), push_back(), peek_front(), peek_back(), pop_front(), pop_back(), insert_after(), insert_before().

# List Node class
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

# Double Linked List class
class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def push_front(self, new_data):
    node = Node(new_data)
    node.next = self.head
    if self.head != None:
        self.head.prev = node
        self.head = node
        node.prev = None
    else:
      self.head = node
      self.tail = node
      node.prev = None
    
  def push_back(self, new_data):
      node = Node(new_data)
      node.prev = self.tail
      if self.tail == None:
        self.head = node 
        self.tail = node
        node.next = None    
      else:
        self.tail.next = node
        node.next = None
        self.tail = node
    

  def peek_front(self):
    if self.head == None:
      print("List is empty")
    else:
      return self.head.data

  
  def peek_back(self):
    if self.tail == None:
      print("List is empty")
    else:
      return self.tail.data
  
  def pop_front(self):
    if self.head == None:
      print("List is empty")
    else:
      temp = self.head
      temp.next.prev = None
      self.head = temp.next
      temp.next = None
      return temp.data
  
  def pop_back(self):
    if self.tail == None:
      print("List is empty")
    else:
      temp = self.tail
      temp.prev.next = None
      self.tail = temp.prev
      temp.prev = None
      return temp.data

  def insert_after(self, temp_node, new_data):
    if temp_node == None:
      print("Given node is empty")
    if temp_node != None:
      node = Node(new_data)
      node.next = temp_node.next
      temp_node.next = node
      node.prev = temp_node
      if node.next != None:
        node.next.prev = node
      if temp_node == self.tail:
        self.tail = node
  
  def insert_before(self, temp_node, new_data):
    if temp_node == None:
      print("Given node is empty")
    if temp_node != None:
      node = Node(new_data)
      node.prev = temp_node.prev
      temp_node.prev = node
      node.next = temp_node
      if node.prev != None:
        node.prev.next = node
      if temp_node == self.head:
        self.head = node
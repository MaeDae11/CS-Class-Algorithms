class LinkedListNode:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.right = None
    self.left = None

class LinkedList:
  def __init__(self):
    self.start = None
    self.end = None

  def append(self, key, value):
    new_node = LinkedListNode(key, value)

    if self.start is None:
      self.start = new_node
      self.end = new_node
    else:
      self.end.right = new_node
      new_node.left = self.end
      self.end = new_node


class MyHashTable:
  def __init__(self):
    self.my_array = [None] * 26

  def put(self, key, value):
    index = self.my_hash_function(key)
    # if bucket is none, we are going to create a new instance
    if self.my_array[index] == None:
      self.my_array[index] = LinkedList()

    # returns a linked list so can append
    self.my_array[index].append(key, value)

  def get(self, key):
    index = self.my_hash_function(key)  

    if self.my_array[index] is None:
      return None

    linked_list = self.my_array[index]
    # loop through linked list
    current_node = linked_list.start

    while current_node != None:
      # value is value of the node
      # better if value was named key
      if current_node.key == key:
        return current_node
      current_node = current_node.right


  def my_hash_function(self, input_value):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    first_letter = input_value[0]
    return alphabet.index(first_letter)


hash_table = MyHashTable()


hash_table.put('first_name', 'Bob')
print hash_table.my_array[5].start.value
# OR a better way is using our get function! :)
print hash_table.get('first_name').value

# HashTables!
# Twitter uses Hashtables
# combines benefits of arrays and linked list
  # random access
# adding and removing from linked list is consistent
# if need to do something in 'real time' then you want a hash table
# downside:
  # take a lot of memory
  # ex: our hash table has 26 spots (a-z) therefore there will always have to be 26 spots
    # larger ones take up a lot of memory
    # real world hash tables have millions of options so store 1/4 until needed to expand
class MyQueue:
  def __init__(self):
    self.queue = []
  
  def enqueue(self, new_element):
    # adds the new element to the end of the array 
    # similar to push method
    self.queue.append(new_element)
    print self.queue

  def dequeue(self):
    # Removes the first element from the array
    del self.queue[0]
    print self.queue

q = MyQueue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
q.dequeue()
q.enqueue(12)

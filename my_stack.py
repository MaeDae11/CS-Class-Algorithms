
# excersice showcasing inner workings of push, pop and peek
class MyStack:
  def __init__(self):
    self.stack = []

  def push(self, new_element):
    # adds new element to the top of the stack
    self.stack.append(new_element)
    pass

  def pop(self):
    # Remove the top most element and also return it
    last_index = len(self.stack) - 1
    element = self.stack[last_index]
    del self.stack[last_index]
    return element

  def peek(self):
    # Return the top most element
    last_index = len(self.stack) - 1
    return self.stack[last_index]


s = MyStack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.pop()
s.peek()

print s.stack
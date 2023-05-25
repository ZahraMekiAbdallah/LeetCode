class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
      self.stack.append(val)
      if (len(self.min_stack) > 0 and val < self.min_stack[-1]) or (len(self.min_stack) == 0):
          self.min_stack.append(val)       
      else:
        self.min_stack.append(self.min_stack[-1]) # adding same value to handle in pop() 
        
    def pop(self) -> None:
      self.stack.pop()
      self.min_stack.pop()
          
    def top(self) -> int:
      return self.stack[-1]

    def getMin(self) -> int:
      if len(self.min_stack) > 0:
        return self.min_stack[-1] 
      else:
        return False


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
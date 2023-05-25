class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      stack = []
      
      for i in range(len(tokens)):        
        if tokens[i] not in ['+','-','*','/']:
          stack.append(int(tokens[i]))
        else:
          item2, item1 = stack.pop(), stack.pop()
          
          if tokens[i]  == '+':
            stack.append(item1 + item2)
          elif tokens[i]  == '*':
            stack.append(int(item1 * item2))
          elif tokens[i]  == '-':
            stack.append(item1 - item2)
          elif tokens[i]  == '/':
            stack.append(int(item1 / item2))
      
      return stack[0]
            
              
        
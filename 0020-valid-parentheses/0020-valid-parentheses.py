class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      
      for i in range(len(s)):
        if s[i] in ['(', '{', '[']:
          stack.append(s[i])
        else:
          if len(stack) > 0:
            last_open = stack.pop()
            if (s[i] == ')' and last_open != '(') or (s[i] == ']' and last_open != '[') or (s[i] == '}' and last_open != '{'):
              return False
          else:
            return False
      return len(stack) == 0

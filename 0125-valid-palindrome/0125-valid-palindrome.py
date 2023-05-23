class Solution:
    def isPalindrome(self, s: str) -> bool:
      res = []
      for i in range(len(s)):
        if s[i].isalpha() or s[i].isnumeric():
          res.append(s[i].lower())
          
      if res == res[::-1]:
        return True
      
      return False

        
# Test Case
# "0P"

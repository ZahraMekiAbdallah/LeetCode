class Solution:
    def isPalindrome(self, s: str) -> bool:
      # Two pointers
      l, r = 0, len(s)-1
      
      while l < r:
        if s[l].isalnum() and s[r].isalnum():
          if s[l].lower() == s[r].lower(): 
            l+=1
            r-=1
          else:
            return False
          
        if not s[l].isalnum():
          l+=1
        
        if not s[r].isalnum():
          r-=1
          
      return True

        
# Test Case
# "0P"

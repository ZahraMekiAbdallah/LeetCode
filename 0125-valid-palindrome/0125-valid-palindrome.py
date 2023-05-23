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
        elif not s[l].isalnum() and s[r].isalnum():
          l+=1
        elif not s[r].isalnum() and s[l].isalnum():
          r-=1
        else:
          l+=1
          r-=1
          
      return True

        
# Test Case
# "0P"

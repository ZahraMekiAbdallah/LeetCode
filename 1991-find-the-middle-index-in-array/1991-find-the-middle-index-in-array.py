import numpy as np

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        
        for i in range(len(nums)):
          if right-nums[i] == left:
            return i
          
          left += nums[i]
          right -= nums[i]
            
        return -1
        
  

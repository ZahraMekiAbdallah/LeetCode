class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
          while nums[i]-1 != i and nums[i] != 0:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1] 
                    
        for i in range(len(nums)):
          if nums[i] == 0:
            return i+1
          
        return 0
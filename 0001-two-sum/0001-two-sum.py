class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
          reset = target - nums[i]
          if reset in dic:
            return [i, dic[reset]]
          dic[nums[i]] = i
          
        #=== Solution 1 ===========================         
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i]+nums[j]) == target:
        #             return [i, j]
        
        #=== Solution 2 =============================
        # for i in range(len(nums)): #O(n)
        #   reset = target - nums[i]
        #   if reset in nums and nums.index(reset) != i: #O(n) for "in" 
        #     return [i, nums.index(reset)]
        
        #=== Solution 3 =============================
        # dic = {}
        # for i in range(len(nums)):  #O(n)
        #   dic[nums[i]] = i
        # for i in range(len(nums)):  #O(n)
        #   reset = (target - nums[i])
        #   if reset in dic and dic[reset] != i:
        #     return [i, dic[reset]]
        #=========================================

            
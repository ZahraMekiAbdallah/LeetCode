from collections import defaultdict 

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(list)
        for i in range(len(nums)):
          if dic.get(nums[i]):
            for val in dic[nums[i]]:
              if abs(val-i) <= k:
                return True
          dic[nums[i]].append(i)
                
        return False
        
        
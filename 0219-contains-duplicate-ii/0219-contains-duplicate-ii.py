from collections import defaultdict 

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(list)
        for i in range(len(nums)):
          dic[nums[i]].append(i)
        
        for key, v in dic.items():
          if len(v) > 1:
            for i in range(len(v)):
              for j in range(i+1, len(v)):
                if abs(v[i]-v[j]) <= k:
                  return True
                
        return False
        
        
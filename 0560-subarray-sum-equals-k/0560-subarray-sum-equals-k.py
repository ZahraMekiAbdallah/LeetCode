class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      total = 0
      res = 0
      dic = {0: 1}
      
      for n in nums:
        total += n
        diff = total - k
        res += dic.get(diff, 0)
        dic[total] = 1 + dic.get(total, 0)
        
      return res
        
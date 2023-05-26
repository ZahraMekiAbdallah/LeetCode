from heapq import heappop, heappush

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      ''' You must solve it in O(n) time complexity using "Priority queue" '''
      min_q = []
      
      for i in range(len(nums)):
        heappush(min_q, nums[i])
        if len(min_q) > k:
          heappop(min_q)
        
      return min_q[0] if len(min_q) > 0 else -1
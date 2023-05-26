class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
      '''You must solve the problem without modifying the array nums and 
        uses only constant extra space.
        nums.length == n + 1, 1 <= nums[i] <= n 
        [Floyd's Tortoise and Hare (Cycle Detection)]
        Space complexity O(1) + nums not modified'''
      
      slow, fast = nums[0], nums[0]
      
      while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
          break
          
      slow = nums[0]
      while fast != slow:
        slow = nums[slow]
        fast = nums[fast]
      
      return fast
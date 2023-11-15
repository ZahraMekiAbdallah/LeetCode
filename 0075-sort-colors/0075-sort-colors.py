class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i< len(nums):
            if nums[i] > nums[-1]:
                nums[i], nums[-1] = nums[-1], nums[i]
            nums = self.check_prev(nums, i)
            i+=1
                
    def check_prev(self, nums, idx):
        for i in range(idx+1):
            if nums[i] > nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
        return nums
        
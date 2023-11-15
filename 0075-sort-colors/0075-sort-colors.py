class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, k = 0, len(nums)-1
        
        while k >= 0:
            for i in range(k):
                j = i+1
                if nums[i] > nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
                i+=1
            k-=1
        
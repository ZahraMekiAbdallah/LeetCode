class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = math.inf
        res = 0
        
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r and r < len(nums):
                sum_num = nums[i]+nums[l]+nums[r]
                if diff > abs(target-sum_num):
                    res = sum_num
                    diff = abs(target-sum_num)
                if sum_num > target:
                    r-=1
                elif sum_num < target:
                    l+=1
                else:
                    return target
                
        return res

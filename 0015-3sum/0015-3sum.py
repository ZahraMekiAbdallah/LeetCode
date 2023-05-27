class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # Sorted to use 2 pointers and get the sum to decrease or increase l, r
        for i in range(len(nums)-2):
            if (nums[i] != nums[i-1] and i > 0) or i == 0:# if number duplicated
                l = i+1
                r = len(nums)-1
                while l < r:
                    if nums[i]+nums[l]+nums[r] > 0:
                        r-=1
                        while  i < r < len(nums)-1 and nums[r] == nums[r+1]:
                          r-=1
                    else:
                        if nums[i]+nums[l]+nums[r] == 0:
                          res.append([nums[i],nums[l],nums[r]])
                        l+=1
                        
                        while i < l < r and nums[l] == nums[l-1]:
                          l+=1
                                
        return res

            
        
      
        
            
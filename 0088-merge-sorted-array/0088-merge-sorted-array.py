class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Edge Case 
        if n == 0:
            return
              
        nums1[m:] = nums2
        
        k = len(nums1)-1
        
        while k > 0:
            for i in range(k):
                j = i+1
                if nums1[i] > nums1[j]:
                    nums1[i], nums1[j] = nums1[j], nums1[i]
            k -= 1

            
                
            
               
                
        
        
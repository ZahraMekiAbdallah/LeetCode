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

                
        i, j = 0, 0
        while i < len(nums1) and j < n:
            if nums1[i] > nums2[j]:
                nums1.pop() # remove zero
                nums1.insert(i, nums2[j]) #swap
                nums2[j] = 0
                j+=1
            i+=1
        
        n-=1
        for i in range(len(nums1)-1, -1, -1):
            if nums1[i] == 0 and nums2[n] != 0:
                nums1[i] = nums2[n]
                n-=1
            else:
                break

            
                
            
               
                
        
        
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
                nums1.insert(i, nums2[j]) 
                nums2[j] = 0
                j+=1
                i+=1
            elif nums1[i] <= nums2[j]:
                i+=1
        
        temp = []
        for n in nums2:
            if n != 0:
                temp.append(n)
                nums1.pop()
                
        if len(temp) > 0:
            nums1.extend(temp)

            
                
            
               
                
        
        
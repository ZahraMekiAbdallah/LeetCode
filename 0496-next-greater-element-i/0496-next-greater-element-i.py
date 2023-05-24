from collections import Counter
class Solution:    
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
      res = []
      dic = {}
      for i in range(len(nums2)):
        dic[nums2[i]] = i
              
      for i in range(len(nums1)):
        found = False
        for j in range(dic[nums1[i]]+1, len(nums2)):
          if nums2[j] > nums1[i]:
            found = True
            res.append(nums2[j])
            break
        if not found:
          res.append(-1)
        
      return res
        
      
        
    
    
    
    
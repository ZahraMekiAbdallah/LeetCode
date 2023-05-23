# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def mergeTwoLists(self, ls1: Optional[ListNode], ls2: Optional[ListNode]) -> Optional[ListNode]:

      if not ls1 or not ls2:
        return ls1 if ls1 else ls2
      
      
      ls = ListNode(0)
      pointer = ls
      
      while ls2 and ls1:        
        if ls1.val <= ls2.val:
          pointer.next = ls1
          pointer = pointer.next
          ls1 = ls1.next
        else:
          pointer.next = ls2
          pointer = pointer.next
          ls2 = ls2.next    
      
      if ls1:
        pointer.next = ls1
      if ls2:
        pointer.next = ls2
      
      return ls.next
    
# Test Case:
# [5], [1,2,4]
                
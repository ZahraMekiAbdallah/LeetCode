# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #eadge case
        if not head:
          return head
        
        mid_node = self.get_middle_node(head)
        prev = self.reverse_second_part(mid_node)
        
        curr = head

        while prev and curr:
          c_nxt = curr.next
          p_nxt = prev.next 
          curr.next = prev
          prev.next = c_nxt
          curr = c_nxt
          prev = p_nxt
        
    def reverse_second_part(self, mid_node):
        pointer = mid_node
        prev = None
        while pointer:
          next_temp = pointer.next
          pointer.next = prev
          prev = pointer
          pointer = next_temp
        return prev

        
    def get_middle_node(self, head):
        slow, fast = head, head.next
        
        while fast and fast.next:
          slow = slow.next
          fast = fast.next.next
          
        return slow
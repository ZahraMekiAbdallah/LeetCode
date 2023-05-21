# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
          return False
        
        #Fast & Slow Pointers
        slow, fast = head, head.next
        
        while slow != fast and fast and fast.next:
          slow = slow.next
          fast = fast.next.next
        
        return fast == slow

        
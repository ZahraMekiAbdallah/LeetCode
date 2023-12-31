class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l3 = ListNode()
        p3 = l3
        remain = 0
        
        while l1 or l2 or remain > 0:
            num = remain
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
                
            remain = num // 10
            p3.next = ListNode(num % 10)
            p3 = p3.next
        
        return l3.next
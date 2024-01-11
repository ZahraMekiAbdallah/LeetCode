class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        ls1 = lists[0] 
        for i in range(1, len(lists)):
            ls1 = self.mergeTwoLists(ls1, lists[i])
        return ls1

    def mergeTwoLists(self, ls1, ls2):
        ls3 = ListNode()
        p1, p2, p3 = ls1, ls2, ls3
        
        while p1 and p2:
            if p1.val <= p2.val:
                p3.next = p1
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next
            p3 = p3.next

        if p1:
            p3.next = p1
        if p2:
            p3.next = p2

        return ls3.next 
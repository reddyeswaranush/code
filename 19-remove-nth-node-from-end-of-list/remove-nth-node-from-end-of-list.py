class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp1 = head
        temp2 = head
        while n:
            n -= 1
            temp1 = temp1.next
        
        if temp1 is None:
            return head.next
        
        while temp1.next is not None:
            temp1 = temp1.next
            temp2 = temp2.next
        
        temp2.next = temp2.next.next
        return head

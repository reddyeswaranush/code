class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        max_val = prev.val
        curr = prev
        filtered = curr
        
        while curr.next:
            if curr.next.val < max_val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_val = curr.val
        
        prev2 = None
        curr = filtered
        while curr:
            nxt = curr.next
            curr.next = prev2
            prev2 = curr
            curr = nxt
        
        return prev2
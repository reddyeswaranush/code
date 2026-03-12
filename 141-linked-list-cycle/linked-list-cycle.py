# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp1=head
        temp2=head
        if temp1==None or temp1.next==None:
            return False
        while temp2!=None and temp2.next!=None:
            temp1=temp1.next
            temp2=temp2.next.next
            if temp1==temp2:
                return True
        return False 
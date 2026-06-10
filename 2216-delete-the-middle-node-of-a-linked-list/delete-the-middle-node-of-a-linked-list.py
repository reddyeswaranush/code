# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return None
        temp1=head
        temp2=head.next.next
        while temp2 and temp2.next:
            temp1=temp1.next
            temp2=temp2.next.next
        if temp1.next:
            temp1.next=temp1.next.next
        else:
            temp1.next=None
        return head
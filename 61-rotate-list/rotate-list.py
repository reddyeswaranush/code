# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None or k==0:
            return head
        a=1
        temp=head
        while temp.next:
            a+=1
            temp=temp.next
        k=k%a
        if k==0:
            return head
        temp.next=head
        temp1=head
        for _ in range(a-k-1):
            temp1=temp1.next
        head=temp1.next
        temp1.next=None
        return head
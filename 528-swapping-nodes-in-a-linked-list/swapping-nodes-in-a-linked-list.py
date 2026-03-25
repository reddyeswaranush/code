# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a=0
        temp=head
        while temp!=None:
            temp=temp.next
            a+=1

        temp1=head
        temp2=head
        a=a-k
        while k-1:
            temp1=temp1.next
            k=k-1
        
        while a:
            temp2=temp2.next
            a=a-1
        
        x=temp1.val
        temp1.val=temp2.val
        temp2.val=x
        return head
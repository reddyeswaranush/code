# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp1=head
        temp2=None
        while temp1:
            temp3=temp1.next
            temp1.next=temp2
            temp2=temp1
            temp1=temp3
        return temp2
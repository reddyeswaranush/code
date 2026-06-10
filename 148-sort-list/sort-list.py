# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        a=[]
        temp=head
        while temp:
            a.append(temp.val)
            temp=temp.next
        a.sort()
        temp1=ListNode(a[0])
        temp2=temp1
        for i in a[1:]:
            temp3=ListNode(i)
            temp2.next=temp3
            temp2=temp2.next
        temp2.next=None
        return temp1
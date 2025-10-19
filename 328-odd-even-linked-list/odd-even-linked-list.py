# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i=0
        even=[]
        odd=[]
        if head==None:
            return head
        temp=head
        while temp!=None:
            if i%2==0:
                odd.append(temp.val)
                temp=temp.next
                i+=1
            else:
                even.append(temp.val)
                temp=temp.next
                i+=1
        nos=odd+even
        head1=ListNode()
        head1.val=nos[0]
        temp=head1
        for i in nos[1:]:
            new=ListNode(i)
            temp.next=new
            temp=temp.next
        return head1
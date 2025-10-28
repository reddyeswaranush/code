# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #if the node is none thenn there is no need to reverse it 
        if head==None:
            return 
        #prev is used to store the previous node
        prev=None
        #temp is used to store the present value
        temp=head
        #we will run it until the temp.next is none as the tem.next.next value does not exist so where we try to get it its gives error
        while temp.next:
            #next is used to store the next node
            nex=temp.next
            #we break the exsisting next pointer
            temp.next=prev
            #we taverse the prev
            prev=temp
            temp=nex
        #as we did not connect the last node so we connect it hear
        temp.next=prev
        return temp
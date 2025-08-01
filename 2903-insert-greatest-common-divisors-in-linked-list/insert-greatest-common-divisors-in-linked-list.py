# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=head
        if node.next==None:
            return node
        x=[]
        while node.next!=None:
            x.append(node.val)
            x.append(math.gcd(node.val,node.next.val))
            node=node.next
        x.append(node.val)
        head1=ListNode(x[0])
        cur=head1
        for i in x[1:]:
            cur.next=ListNode(i)
            cur=cur.next
        return head1
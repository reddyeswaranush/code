# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        x=[]
        temp=head
        if temp==None or temp.next==None:
            return False
        while temp!=None:
            if temp not in x:
                x.append(temp)
                temp=temp.next
            else:
                return True
        return False
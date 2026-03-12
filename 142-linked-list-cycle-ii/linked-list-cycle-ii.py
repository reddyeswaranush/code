# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = head
        temp2 = head
        
        while temp2 != None and temp2.next != None:
            temp1 = temp1.next
            temp2 = temp2.next.next
            
            if temp1 == temp2:
                temp1 = head
                while temp1 != temp2:
                    temp1 = temp1.next
                    temp2 = temp2.next
                return temp1
        return None
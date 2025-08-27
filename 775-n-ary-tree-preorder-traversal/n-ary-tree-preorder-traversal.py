"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        x=[]
        def ans(a):
            if not a:
                return
            x.append(a.val)
            for i in a.children:
                ans(i)
        ans(root)
        return x
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        q=[root]
        x=[]
        while q:
            a=len(q)
            b=[]
            for _ in range(a):
                c=q.pop(0)
                b.append(c.val)
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
            x.append(b)
        return x
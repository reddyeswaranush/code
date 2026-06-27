# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        x=[]
        q=[root]
        while q:
            c=q.pop()
            x.append(c.val)
            if c.right:
                q.append(c.right)
            if c.left:
                q.append(c.left)
        return x
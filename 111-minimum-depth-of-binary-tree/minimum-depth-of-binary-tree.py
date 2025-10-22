# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        def ans(root,i):
            if root==None:
                return float('inf')
            if root.left==None and root.right==None:
                return 0
            l=ans(root.left,i)
            r=ans(root.right,i)
            return min(l,r)+1
        return ans(root,0)+1
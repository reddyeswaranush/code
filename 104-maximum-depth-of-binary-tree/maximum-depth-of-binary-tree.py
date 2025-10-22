# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def ans(root,i):
            if root==None:
                return 0
            l=ans(root.left,i+1)
            r=ans(root.right,i+1)
            return max(l,r)+1
        return ans(root,0)
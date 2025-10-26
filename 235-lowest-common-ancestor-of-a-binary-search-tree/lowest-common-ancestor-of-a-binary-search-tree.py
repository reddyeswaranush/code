# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def ans(root):
            if root==None or root==q or root==p:
                return root
            left=ans(root.left)
            right=ans(root.right)
            if not left:
                return right
            elif not right:
                return left
            else:
                return root
        return ans(root)
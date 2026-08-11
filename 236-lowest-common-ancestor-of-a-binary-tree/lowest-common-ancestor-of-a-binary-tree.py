# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(root):
            if root==None or root==q or root==p:
                return root
            left=search(root.left)
            right=search(root.right)
            if left and right:
                return root
            if left!=None:
                return left
            if right!=None:
                return right
        return search(root)
        
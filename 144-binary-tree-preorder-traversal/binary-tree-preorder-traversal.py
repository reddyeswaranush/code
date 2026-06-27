# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        x=[]
        def help(root):
            if root==None:
                return 
            x.append(root.val)
            help(root.left)
            help(root.right)
        help(root)
        return x
        
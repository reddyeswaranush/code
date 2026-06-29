# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        a=[]
        def help(root):
            if root==None:
                return 0
            left=help(root.left)
            right=help(root.right)
            a.append(left+right)
            return max(left,right)+1
        help(root)
        return max(a) if len(a)!=0 else 0
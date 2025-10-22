# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        x=[]
        def check(root):
            if root==None:
                return 0
            left=check(root.left)
            right=check(root.right)
            x.append(left+right)
            return max(left,right)+1
        check(root)
        if x==[]:
            return 0
        else:
            return max(x)
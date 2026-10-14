# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        x=[]
        def search(root):
            if root==None:
                return 0
            left=search(root.left)
            right=search(root.right)
            x.append(left+right)
            return max(left,right)+1
        search(root)
        return max(x)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def ans(root,minn,maxx):
            if root==None:
                return True
            if root.val<=minn or root.val>=maxx:
                return False
            left=ans(root.left,minn,root.val)
            right=ans(root.right,root.val,maxx)
            return left and right
        return ans(root,float('-inf'),float('inf'))
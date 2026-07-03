# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def help(root,mi,ma):
            if root==None:
                return True
            left=help(root.left,mi,root.val)
            right=help(root.right,root.val,ma)
            if left and right:
                if mi<root.val<ma:
                    return True
                else:
                    return False
            else:
                return False
        return help(root,float('-inf'),float('inf'))
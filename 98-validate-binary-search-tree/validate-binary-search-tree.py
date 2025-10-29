# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def ans(root,min_val,max_val):
            if root==None:
                return True
            left=ans(root.left,min_val,root.val)
            right=ans(root.right,root.val,max_val)
            if left and right:
                if min_val<root.val<max_val:
                    return True
                else:
                    return False
            else:
                return False
        return ans(root,float('-inf'),float('inf'))
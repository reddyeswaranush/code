# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return 1
            l=check(root.left)
            r=check(root.right)
            if l==-1 or r==-1 or abs(l-r)>1:
                return -1
            return max(l,r)+1
        return check(root)!=-1         
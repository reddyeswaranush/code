# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        x=[0]
        def check(root):
            if not root:
                return 0
            l=check(root.left)
            r=check(root.right)
            x.append(l+r)
            return max(l,r)+1
        check(root)
        return max(x)
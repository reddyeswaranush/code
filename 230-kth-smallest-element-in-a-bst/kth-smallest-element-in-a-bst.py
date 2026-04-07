# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        x=[]
        def ans(root):
            if root==None:
                return []
            ans(root.left)
            x.append(root.val)
            ans(root.right)
            return x
        a=ans(root)
        a.sort()
        return a[k-1]
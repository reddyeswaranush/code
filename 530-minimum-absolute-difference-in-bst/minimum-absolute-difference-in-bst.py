# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        x=[]
        def ans(root):
            if root==None:
                return 
            ans(root.left)
            x.append(root.val)
            ans(root.right)
        ans(root)
        minn=float("inf")
        for i in range(1,len(x)):
            minn=min(minn,abs(x[i]-x[i-1]))
        return minn
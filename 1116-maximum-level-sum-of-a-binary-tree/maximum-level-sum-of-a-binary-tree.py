# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        x=[]
        q=[root]
        while q:
            a=len(q)
            b=0
            for i in range(a):
                p=q.pop(0)
                b+=p.val
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
            x.append(b)
        return x.index(max(x))+1
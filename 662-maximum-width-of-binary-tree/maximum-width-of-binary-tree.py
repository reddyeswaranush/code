# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q=[(root,0)]
        m=0
        while q:
            a=len(q)
            first=0
            last=0
            mi=q[0][1]
            for i in range(a):
                b=q.pop(0)
                curr=b[1]-mi
                if i==0:
                    first=curr
                if i==a-1:
                    last=curr
                if b[0].left:
                    q.append((b[0].left,2*curr+1))
                if b[0].right:
                    q.append((b[0].right,2*curr+2))
            m=max(m,last-first+1)
        return m
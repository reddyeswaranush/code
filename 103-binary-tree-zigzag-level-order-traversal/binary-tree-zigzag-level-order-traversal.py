# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        q=[root]
        x=[]
        a=0
        while q:
            b=len(q)
            c=[]
            for _ in range(b):
                d=q.pop(0)
                c.append(d.val)
                if d.left:
                    q.append(d.left)
                if d.right:
                    q.append(d.right)
            if a%2==0:
                x.append(c)
            else:
                x.append(c[::-1])
            a+=1
        return x
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(root):
            x=[]
            q=[root]
            while q:
                a=len(q)
                for i in range(a):
                    node=q.pop(0)
                    if node==None:
                        x.append("null")
                    else:
                        x.append(node.val)
                        q.append(node.left)    
                        q.append(node.right)
            return x
        return check(p)==check(q)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result=[]
        queue=[]
        queue.append(root)
        while queue:
            a=len(queue)
            b=[]
            for _ in range(a):
                c=queue.pop(0)
                b.append(c.val)
                if c.left:
                    queue.append(c.left)
                if c.right:
                    queue.append(c.right)
            result.append(b)
        return len(result)
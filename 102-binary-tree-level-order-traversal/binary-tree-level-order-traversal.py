# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        if root==None:
            return result
        queue=[]
        queue.append(root)
        while queue:
            a=len(queue)
            subans=[]
            for _ in range(a):
                b=queue.pop(0)
                subans.append(b.val)
                if b.left:
                    queue.append(b.left)
                if b.right:
                    queue.append(b.right)
            result.append(subans)
        return result
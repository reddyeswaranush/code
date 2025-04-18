# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left = []
        right = []

        q = [root.left]
        p = [root.right]

        while q:
            node = q.pop(0)
            if node:
                left.append(node.val)
                q.append(node.right)
                q.append(node.left)
            else:
                left.append(None)

        while p:
            node = p.pop(0)
            if node:
                right.append(node.val)
                p.append(node.left)
                p.append(node.right)
            else:
                right.append(None)

        return left == right
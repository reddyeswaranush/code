# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node=TreeNode(val)
        root1=root
        if root==None:
            return node
        while True:
            if root1.val>val:
                if root1.left is None:
                    root1.left=node
                    break
                root1=root1.left
            else:
                if root1.right is None:
                    root1.right=node
                    break
                root1=root1.right
        return root
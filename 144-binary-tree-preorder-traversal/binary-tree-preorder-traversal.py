# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a=[]
        if root==None:
            return []
        a.append(root.val)
        a+=self.preorderTraversal(root.left)
        a+=self.preorderTraversal(root.right)
        return a
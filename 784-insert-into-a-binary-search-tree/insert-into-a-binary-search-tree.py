# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            return TreeNode(val)
        v=TreeNode(val)
        temp=root
        while True:
            if temp.val<v.val:
                if not temp.right:
                    temp.right=v
                    break
                else:
                    temp=temp.right
            if temp.val>v.val:
                if not temp.left:
                    temp.left=v
                    break
                else:
                    temp=temp.left
        return root
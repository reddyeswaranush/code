# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def help(root):
            if root==None:
                return 0
            total=0
            le=0
            ri=0
            temp1=root
            temp2=root
            while temp1:
                le+=1
                temp1=temp1.left
            while temp2:
                ri+=1
                temp2=temp2.right
            if le==ri:
                total=2**le-1
            else:
                le_se=help(root.left) if root.left else 0
                ri_se=help(root.right) if root.right else 0
                total=1+le_se+ri_se
            return total
        return help(root)
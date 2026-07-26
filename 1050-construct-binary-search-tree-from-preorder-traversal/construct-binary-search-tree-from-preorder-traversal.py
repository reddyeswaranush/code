# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        n=len(preorder)
        def ans(i,j):
            if i>j:
                return None
            root=TreeNode(preorder[i])
            k=i+1
            while k<=j and preorder[i]>preorder[k]:
                k+=1
            root.left=ans(i+1,k-1)
            root.right=ans(k,j)
            return root
        return ans(0,n-1)
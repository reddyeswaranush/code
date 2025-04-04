# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return None, 0
            left_tree, left_depth = helper(node.left)
            right_tree, right_depth = helper(node.right)

            if left_depth > right_depth:
                return left_tree, left_depth + 1

            elif right_depth > left_depth:
                return right_tree, right_depth + 1

            return node, left_depth + 1

        node, depth = helper(root)
        return node
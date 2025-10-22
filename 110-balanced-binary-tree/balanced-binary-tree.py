class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def ans(root):
            if not root:
                return 0
            left = ans(root.left)
            if left == -1:
                return -1
            right = ans(root.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return ans(root) != -1
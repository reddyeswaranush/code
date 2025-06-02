# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check(r):
            s = []
            t = [r]
            while t:
                i = t.pop(0)
                if i is None:
                    s.append(None)  # preserve structure
                    continue
                s.append(i.val)
                t.append(i.left)
                t.append(i.right)
            return s

        def find_all(a):
            if a is None:
                return []
            result = []
            if a.val == subRoot.val:
                result.append(a)
            result += find_all(a.left)
            result += find_all(a.right)
            return result

        candidates = find_all(root)
        for b in candidates:
            if check(b) == check(subRoot):
                return True
        return False
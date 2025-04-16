# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        t = []
        q = [[root, 0, 0]]
        
        while q:
            a = len(q)
            for _ in range(a):
                b = q.pop(0)
                node = b[0]
                t.append([node.val, b[1], b[2]])
                if node.left:
                    q.append([node.left, b[1] + 1, b[2] - 1])
                if node.right:
                    q.append([node.right, b[1] + 1, b[2] + 1])

        s = sorted(t, key=lambda x: (x[2], x[1], x[0]))
        
        d = defaultdict(list)
        for i in s:
            d[i[2]].append(i[0])
        
        x = []
        for key in sorted(d):
            x.append(d[key])
        return x
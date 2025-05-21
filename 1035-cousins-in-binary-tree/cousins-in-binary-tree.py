# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        a={}
        b=root
        d=[b]
        while len(d)>0:
            e=len(d)
            for _ in range(e):
                f=d.pop(0)
                if f.val not in a:
                    a[f.val]=[]
                if f.left:
                    d.append(f.left)
                if f.right:
                    d.append(f.right)
        d.append(b)
        g=0
        while len(d)>0:
            e=len(d)
            for _ in range(e):
                f=d.pop(0)
                if f.left:
                    a[f.left.val].append(f)
                    a[f.left.val].append(g)
                    d.append(f.left)
                if f.right:
                    a[f.right.val].append(f)
                    a[f.right.val].append(g)
                    d.append(f.right)
            g+=1
        if len(a[x])==0 or len(a[y])==0:
            return False
        elif a[x][0]!=a[y][0] and a[x][1]==a[y][1]:
            return True
        else:
            return False
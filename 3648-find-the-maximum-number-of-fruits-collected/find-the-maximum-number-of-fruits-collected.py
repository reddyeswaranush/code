class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        p1=0
        for i in range(len(fruits)):
            p1+=fruits[i][i]

        self.mem={}

        def pp2(i,j):
            if i>=0 and i<len(fruits) and j<len(fruits) and j>=0 and j>i:
                if i==len(fruits) and i==j:
                    return 0
                if (i,j) in self.mem:
                    return self.mem[(i,j)]
                self.mem[(i,j)]=fruits[i][j]+max(pp2(i+1,j),pp2(i+1,j-1),pp2(i+1,j+1))
                return self.mem[(i,j)]
            else:
                return 0

        self.mem1={}

        def pp3(i,j):
            if i>=0 and i<len(fruits) and j<len(fruits) and j>=0 and i>j:
                if i==len(fruits)-1 and i==j:
                    return 0
                if (i,j) in self.mem1:
                    return self.mem1[(i,j)]
                self.mem1[(i,j)]=fruits[i][j]+max(pp3(i-1,j+1),pp3(i,j+1),pp3(i+1,j+1))
                return self.mem1[(i,j)]
            else:
                return 0
                
        p2=pp2(0,len(fruits)-1)
        p3=pp3(len(fruits)-1,0)
        return p1+p2+p3
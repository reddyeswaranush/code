class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        a={}
        ans=0
        left=0
        n=len(fruits)
        for i in range(n):
            if len(a)==2:
                if fruits[i] in a:
                    a[fruits[i]]+=1
                else:
                    while left<i and len(a)==2:
                        a[fruits[left]]-=1
                        if a[fruits[left]]==0:
                            del a[fruits[left]]
                        left+=1
                    a[fruits[i]]=1
            elif len(a)<2:
                if fruits[i] not in a:
                    a[fruits[i]]=0
                a[fruits[i]]+=1
            ans=max(ans,i-left+1)
        ans=max(ans,i-left+1)
        return ans
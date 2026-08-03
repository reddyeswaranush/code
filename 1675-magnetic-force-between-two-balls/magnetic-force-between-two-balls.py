class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left=1
        right=position[-1]-position[0]
        ans=-1
        while left<=right:
            mid=left+(right-left)//2
            last=position[0]
            a=1
            for i in range(1,len(position)):
                if position[i]-last>=mid:
                    a+=1
                    last=position[i]
            if a>=m:
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans
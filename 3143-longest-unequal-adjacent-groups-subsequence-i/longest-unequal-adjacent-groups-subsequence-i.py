class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        y=[]
        y.append([words[0],groups[0]])
        n=len(words)
        for i in range(1,n):
            if y[-1][-1]!=groups[i]:
                y.append([words[i],groups[i]])
        x=[]
        for i in y:
            x.append(i[0])
        return x
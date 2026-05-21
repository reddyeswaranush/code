class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a={}
        for i in strs:
            if "".join(sorted(i)) not in a:
                a["".join(sorted(i))]=[]
            a["".join(sorted(i))].append(i)
        x=[]
        for i in a:
            x.append(a[i])
        return x
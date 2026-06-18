class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapp={2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        x=[]
        def helper(a,ind):
            if ind=='':
                x.append(a)
                return
            for i in mapp[int(ind[0])]:
                helper(a+i,ind[1:])
            return
        helper('',digits)
        return x
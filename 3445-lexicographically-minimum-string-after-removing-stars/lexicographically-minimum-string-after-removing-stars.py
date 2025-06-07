from collections import defaultdict

class Solution:
    def clearStars(self, s: str) -> str:
        x = []
        pos = defaultdict(list)
        for ch in s:
            if ch != '*':
                x.append(ch)
                pos[ch].append(len(x) - 1)
            else:
                for c in map(chr, range(97, 123)):
                    if pos[c]:
                        idx = pos[c].pop()
                        x[idx] = None
                        break

        return ''.join(c for c in x if c is not None)
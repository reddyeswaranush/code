class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(s: str, first: str, second: str, score: int):
            stack = []
            total = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    total += score
                else:
                    stack.append(char)
            return "".join(stack), total

        ans = 0
        if x > y:
            s, gain = remove_pair(s, 'a', 'b', x)
            ans += gain
            _, gain = remove_pair(s, 'b', 'a', y)
            ans += gain
        else:
            s, gain = remove_pair(s, 'b', 'a', y)
            ans += gain
            _, gain = remove_pair(s, 'a', 'b', x)
            ans += gain

        return ans
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        N = len(nums)
        lookup = defaultdict(list)
        for u, v in edges:
            lookup[u].append(v)
            lookup[v].append(u)

        vals = [0] * N
 
        def dfs(u, prev):
            x = nums[u]

            for v in lookup[u]:
                if v == prev:
                    continue

                y = dfs(v, u)
                x ^= y

            vals[u] = x

            return x

        dfs(0, -1)


        pars = [set() for _ in range(N)]

        def dfs2(u, prev, p):
            pars[u] = p.copy()
            p.add(u)
            
            for v in lookup[u]:
                if v == prev:
                    continue

                y = dfs2(v, u, p)

            p.remove(u)


        dfs2(0, -1, set())


        
        best = 10 ** 20

        for i in range(1, N):
            for j in range(i + 1, N):
                if i in pars[j]:
                    x = vals[0]
                    y = vals[i]
                    z = vals[j]
                    x ^= y

                    y ^= z
             
                    best = min(best, max(x, y, z) - min(x, y, z))

                elif j in pars[i]:
                    x = vals[0]
                    y = vals[i]
                    z = vals[j]
                    x ^= z

                    z ^= y


                    best = min(best, max(x, y, z) - min(x, y, z))

                else:
                    x = vals[0]
                    y = vals[i]
                    z = vals[j]
                    x ^= y
                    x ^= z
                    best = min(best, max(x, y, z) - min(x, y, z))


        return best
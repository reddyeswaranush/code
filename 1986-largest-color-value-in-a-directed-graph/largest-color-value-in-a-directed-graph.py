from collections import defaultdict, Counter

class CycleError(Exception):
    pass

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        G = defaultdict(list)
        for a, b in edges:
            G[a].append(b)

        
        visited = set()
        visiting = set()
        topological = []

        def toposort(node):
            if node in visiting:
                raise CycleError()

            visiting.add(node)

            for neighbor in G[node]:
                if neighbor not in visited:
                    toposort(neighbor)

            visiting.remove(node)
            visited.add(node)
            
            topological.append(node)

        for i in range(n):
            if i not in visited:
                try:
                    toposort(i)
                except CycleError:
                    return -1

        visited = set()

        counts = defaultdict(Counter)

        max_count = 0

        for i in topological:
            my_count = counts[i]

            for successor in G[i]:
                my_count |= counts[successor]
            
            my_count[colors[i]] += 1
            my_max_count = max(my_count.values())
            max_count = max(max_count, my_max_count)

        return max_count
class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @cache
        def min_area(r1, r2, c1, c2):
           
            rmin, cmin = m, n
            rmax, cmax = -1, -1
            for r in range(r1, r2):
                for c in range(c1, c2):
                    if grid[r][c]:
                        rmin, cmin = min(rmin, r), min(cmin, c)
                        rmax, cmax = max(rmax, r), max(cmax, c)
            
            if rmax == -1:  # No 1s found
                return 0
            return (rmax - rmin + 1) * (cmax - cmin + 1)
        
        @cache
        def split_once(r1, r2, c1, c2):
            result = float('inf')
          
            for r in range(r1 + 1, r2):
                result = min(result, min_area(r1, r, c1, c2) + min_area(r, r2, c1, c2))
          
            for c in range(c1 + 1, c2):
                result = min(result, min_area(r1, r2, c1, c) + min_area(r1, r2, c, c2))
            return result
        
        @cache
        def split_twice(r1, r2, c1, c2):
            result = float('inf')
            
            for r in range(r1 + 1, r2):
                result = min(result, split_once(r1, r, c1, c2) + min_area(r, r2, c1, c2))
                result = min(result, min_area(r1, r, c1, c2) + split_once(r, r2, c1, c2))
           
            for c in range(c1 + 1, c2):
                result = min(result, split_once(r1, r2, c1, c) + min_area(r1, r2, c, c2))
                result = min(result, min_area(r1, r2, c1, c) + split_once(r1, r2, c, c2))
            return result
        
        return split_twice(0, m, 0, n)
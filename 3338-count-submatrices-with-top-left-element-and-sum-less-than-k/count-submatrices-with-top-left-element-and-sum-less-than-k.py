class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        ps = [[0]*n for _ in range(m)]
        count = 0
        
        for i in range(m):
            for j in range(n):
                ps[i][j] = grid[i][j]
                if i > 0: ps[i][j] += ps[i-1][j]
                if j > 0: ps[i][j] += ps[i][j-1]
                if i > 0 and j > 0: ps[i][j] -= ps[i-1][j-1]
                
                if ps[i][j] <= k:
                    count += 1
        
        return count

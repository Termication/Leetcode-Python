class Solution(object):
    def numberOfPaths(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # Initialize DP table
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        
        # Base case: starting cell
        dp[0][0][grid[0][0] % k] = 1
        
        # Fill DP table
        for i in range(m):
            for j in range(n):
                for r in range(k):
                    if i > 0:
                        newR = (r + grid[i][j]) % k
                        dp[i][j][newR] = (dp[i][j][newR] + dp[i-1][j][r]) % MOD
                    if j > 0:
                        newR = (r + grid[i][j]) % k
                        dp[i][j][newR] = (dp[i][j][newR] + dp[i][j-1][r]) % MOD
        
        # Answer: number of ways to reach bottom-right with remainder 0
        return dp[m-1][n-1][0]
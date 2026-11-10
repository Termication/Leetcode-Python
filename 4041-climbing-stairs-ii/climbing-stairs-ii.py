from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        INF = float("inf")
        dp = [INF] * (n + 1)
        dp[0] = 0

        for j in range(1, n + 1):
            c = costs[j - 1]  # costs is 1-indexed in the problem
            for k in (1, 2, 3):
                i = j - k
                if i >= 0:
                    dp[j] = min(dp[j], dp[i] + c + k * k)

        return dp[n]
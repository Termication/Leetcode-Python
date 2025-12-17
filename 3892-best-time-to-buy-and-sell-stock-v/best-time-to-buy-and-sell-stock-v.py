class Solution(object):
    def maximumProfit(self, prices, k):
        """
        :type prices: List[int]
        :type k: int
        :rtype: int
        """
        NEG_INF = float('-inf')

        # dp[t][0]=neutral, dp[t][1]=long, dp[t][2]=short
        dp = [[0, NEG_INF, NEG_INF] for _ in range(k + 1)]

        for price in prices:
            new_dp = [row[:] for row in dp]

            for t in range(k + 1):
                # Enter positions
                new_dp[t][1] = max(new_dp[t][1], dp[t][0] - price)  # buy
                new_dp[t][2] = max(new_dp[t][2], dp[t][0] + price)  # short sell

                # Exit positions (complete transaction)
                if t + 1 <= k:
                    new_dp[t + 1][0] = max(new_dp[t + 1][0], dp[t][1] + price)  # sell long
                    new_dp[t + 1][0] = max(new_dp[t + 1][0], dp[t][2] - price)  # buy back short

            dp = new_dp

        return max(dp[t][0] for t in range(k + 1))
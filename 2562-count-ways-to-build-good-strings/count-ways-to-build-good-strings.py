class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """
        Counts the number of good strings that can be constructed.

        Args:
            low: The minimum length of a good string.
            high: The maximum length of a good string.
            zero: The number of '0's to append in one step.
            one: The number of '1's to append in one step.

        Returns:
            The number of good strings modulo 10^9 + 7.
        """

        MOD = 10**9 + 7
        dp = [0] * (high + 1)  # dp[i] stores the number of ways to reach length i
        dp[0] = 1  # Base case: empty string

        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % MOD
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % MOD

        count = 0
        for i in range(low, high + 1):
            count = (count + dp[i]) % MOD

        return count
        
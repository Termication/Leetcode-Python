class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Determines if an array can be partitioned into two subsets with equal sum.

        Args:
            nums: A list of integers.

        Returns:
            True if the array can be partitioned, False otherwise.
        """
        total_sum = sum(nums)

        # If the total sum is odd, it cannot be partitioned into two equal sum subsets.
        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2
        n = len(nums)

        # dp[i] will be true if a subset with sum i can be formed using elements from nums.
        dp = [False] * (target_sum + 1)
        dp[0] = True  # An empty subset has a sum of 0.

        # Iterate through each number in nums.
        for num in nums:
            # Iterate backwards through the dp array to avoid using the same number multiple times
            # in the current subset sum calculation.
            for i in range(target_sum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        # If dp[target_sum] is true, it means a subset with the target sum can be formed.
        return dp[target_sum]
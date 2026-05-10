class Solution(object):
    def maximumJumps(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0  # start point
        
        for i in range(n):
            if dp[i] == -1:
                continue
            for j in range(i+1, n):
                if -target <= nums[j] - nums[i] <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
        
        return dp[-1]

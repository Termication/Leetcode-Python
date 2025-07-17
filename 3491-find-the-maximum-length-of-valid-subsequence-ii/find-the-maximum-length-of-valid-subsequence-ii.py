class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        
        overall_max_length = 1

        for target_sum in range(k):
            # dp[r] stores the length of the longest subsequence for the current
            # target_sum, ending with a number where num % k == r.
            dp = [0] * k
            for num in nums:
                current_rem = num % k
                prev_rem = (target_sum - current_rem + k) % k
                dp[current_rem] = 1 + dp[prev_rem]

            overall_max_length = max(overall_max_length, max(dp))
        
        return overall_max_length
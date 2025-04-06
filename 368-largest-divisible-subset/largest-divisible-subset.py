class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []

        nums.sort()  # Sort for easier divisibility check
        dp = [1] * n  # dp[i]: size of largest subset ending with nums[i]
        parent = [-1] * n  # parent[i]: predecessor in largest subset ending with nums[i]
        max_len = 1
        max_index = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        parent[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i

        largest_subset = []
        curr = max_index
        while curr != -1:
            largest_subset.append(nums[curr])
            curr = parent[curr]

        return largest_subset
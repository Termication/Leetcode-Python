class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Compute prefix sum and suffix sum
        prefix_sum = [0] * n
        suffix_sum = [0] * n
        
        # Compute prefix sums
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        
        # Compute suffix sums
        suffix_sum[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + nums[i]
        
        # Step 2: Count valid splits
        valid_splits = 0
        for i in range(n - 1):
            if prefix_sum[i] >= suffix_sum[i + 1]:
                valid_splits += 1
        
        return valid_splits
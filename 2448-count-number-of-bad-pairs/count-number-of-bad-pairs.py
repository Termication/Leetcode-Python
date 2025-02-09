class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n - 1) // 2
        from collections import defaultdict
        counts = defaultdict(int)
        good = 0
        for i in range(n):
            diff = nums[i] - i
            good += counts[diff]
            counts[diff] += 1

        return total - good
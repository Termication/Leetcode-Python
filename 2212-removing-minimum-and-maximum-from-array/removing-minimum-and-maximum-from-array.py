class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        mn = nums.index(min(nums))
        mx = nums.index(max(nums))

        left = min(mn, mx)
        right = max(mn, mx)

        return min(
            right + 1,                # remove both from front
            n - left,                 # remove both from back
            (left + 1) + (n - right) # one from each side
        )
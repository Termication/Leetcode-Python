class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        Calculates the maximum value of an ordered triplet (i, j, k) in the given array.

        Args:
            nums: A list of integers.

        Returns:
            The maximum value of the triplet, or 0 if all triplets have negative values.
        """
        n = len(nums)
        max_value = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    value = (nums[i] - nums[j]) * nums[k]
                    max_value = max(max_value, value)

        return max_value
        
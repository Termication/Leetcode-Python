class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        Calculates the maximum value of an ordered triplet in the given array.

        Args:
            nums: A list of integers.

        Returns:
            The maximum value of an ordered triplet, or 0 if all triplets have negative values.
        """
        n = len(nums)
        max_value = 0
        left_max = [0] * n
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i - 1])

        right_max = [0] * n
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i + 1])

        for j in range(1, n - 1):
            max_value = max(max_value, (left_max[j] - nums[j]) * right_max[j])

        return max_value

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        """
        Calculates the sum of XOR totals for every subset of the given array.

        Args:
            nums: A list of integers.

        Returns:
            The sum of all XOR totals.
        """
        xor_sum = 0
        for num in nums:
            xor_sum |= num
        return xor_sum * (2**(len(nums) - 1))

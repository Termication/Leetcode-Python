class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        """
        Counts the number of pairs (i, j) such that 0 <= i < j < n,
        nums[i] == nums[j], and (i * j) is divisible by k.

        Args:
            nums: A list of integers.
            k: An integer divisor.

        Returns:
            The number of pairs satisfying all conditions.
        """
        count = 0
        n = len(nums)

        if n < 2:
            return 0 # Cannot form pairs if length is less than 2

        # Iterate through all possible pairs (i, j) where i < j
        for i in range(n):
            for j in range(i + 1, n):
                # Check condition 1: Values are equal
                if nums[i] == nums[j]:
                    # Check condition 2: Product of indices is divisible by k
                    if (i * j) % k == 0:
                        count += 1

        return count
        
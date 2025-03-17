class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        """
        Divides an array into equal pairs.

        Args:
            nums: A list of integers.

        Returns:
            True if the array can be divided into equal pairs, False otherwise.
        """
        if len(nums) % 2 != 0:
            return False

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for count in counts.values():
            if count % 2 != 0:
                return False

        return True
        
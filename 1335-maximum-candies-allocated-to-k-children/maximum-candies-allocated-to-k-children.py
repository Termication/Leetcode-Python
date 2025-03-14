class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        """
        Finds the maximum number of candies each child can get.

        Args:
            candies: A list of integers representing the piles of candies.
            k: The number of children.

        Returns:
            The maximum number of candies each child can get.
        """

        def can_allocate(mid):
            count = 0
            for pile in candies:
                count += pile // mid
            return count >= k

        if sum(candies) < k:
            return 0

        left, right = 1, max(candies)
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if can_allocate(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
        
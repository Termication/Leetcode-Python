class Solution:
    def findScore(self, nums: List[int]) -> int:
        """
        Calculate the score of the array after marking all elements.

        Args:
            nums (list[int]): Array of positive integers.

        Returns:
            int: The total score after marking all elements.
        """
        n = len(nums)
        marked = [False] * n  # To track which elements are marked
        score = 0

        # Pair each element with its index and sort by value, then by index
        indexed_nums = sorted((val, idx) for idx, val in enumerate(nums))

        for val, idx in indexed_nums:
            if not marked[idx]:  # If the element is not marked
                score += val  # Add value to score
                # Mark the element and its adjacent elements
                marked[idx] = True
                if idx > 0:  # Mark left neighbor if it exists
                    marked[idx - 1] = True
                if idx < n - 1:  # Mark right neighbor if it exists
                    marked[idx + 1] = True

        return score
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        """
        Calculates the number of possible hidden sequences.

        Args:
            differences: A list of differences between consecutive elements.
            lower: The lower bound for elements in the hidden sequence.
            upper: The upper bound for elements in the hidden sequence.

        Returns:
            The number of possible hidden sequences.
        """
        current_sum = 0  # Python integers handle arbitrary size
        min_prefix_sum = 0
        max_prefix_sum = 0

        for diff in differences:
            current_sum += diff
            min_prefix_sum = min(min_prefix_sum, current_sum)
            max_prefix_sum = max(max_prefix_sum, current_sum)

        # Determine the valid range for the starting element hidden[0]
        # We need:
        # lower <= hidden[0] + min_prefix_sum
        # hidden[0] + max_prefix_sum <= upper
        #
        # This gives:
        # hidden[0] >= lower - min_prefix_sum
        # hidden[0] <= upper - max_prefix_sum

        min_possible_h0 = lower - min_prefix_sum
        max_possible_h0 = upper - max_prefix_sum

        # Calculate the number of integers in the range [min_possible_h0, max_possible_h0]
        if max_possible_h0 < min_possible_h0:
            return 0
        else:
            # The count is (max_possible_h0 - min_possible_h0 + 1)
            count = max_possible_h0 - min_possible_h0 + 1
            return count

        # Or more concisely:
        # return max(0, max_possible_h0 - min_possible_h0 + 1)
        
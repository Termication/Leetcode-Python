class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        """
        Counts the number of good subarrays using a sliding window approach.

        Args:
            nums: The input list of integers.
            k: The minimum number of pairs required for a subarray to be good.

        Returns:
            The total count of good subarrays.
        """
        n = len(nums)
        if k <= 0: # If k is 0 or less, any non-empty subarray is good? Check constraints. Assuming k>=1 based on
            return n * (n + 1) // 2 if k == 0 else 0 # Or handle based on constraints if k=0 is possible

        left = 0
        current_pairs = 0
        total_good_subarrays = 0
        freq = collections.defaultdict(int)

        for right in range(n):
            num_right = nums[right]

            # Add nums[right] to the window and update pairs
            current_pairs += freq[num_right] # Adds pairs formed with existing num_right
            freq[num_right] += 1

            # Shrink window from left if condition is met or exceeded
            # We want the smallest window [left, right] with < k pairs
            # So keep shrinking while pairs >= k
            while current_pairs >= k:
                num_left = nums[left]
                # Remove nums[left] from the window and update pairs
                freq[num_left] -= 1 # Decrement count first
                current_pairs -= freq[num_left] # Subtract pairs it formed (using the new count)
                left += 1

            total_good_subarrays += left

        return total_good_subarrays
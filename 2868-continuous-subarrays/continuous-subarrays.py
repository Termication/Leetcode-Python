class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        """
        Calculate the total number of continuous subarrays.

        Args:
            nums (list[int]): The input array.

        Returns:
            int: Total number of continuous subarrays.
        """
        from collections import deque

        n = len(nums)
        left = 0
        total = 0

        # Deques to keep track of max and min in the current window
        max_deque = deque()
        min_deque = deque()

        for right in range(n):
            # Update the max deque
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)

            # Update the min deque
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)

            # Ensure the condition |max - min| <= 2
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                # Increment left pointer
                left += 1
                # Remove indices out of bounds
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()

            # Count subarrays ending at 'right'
            total += right - left + 1

        return total
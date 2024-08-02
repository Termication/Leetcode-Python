class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Count the total number of 1's
        total_ones = sum(nums)
        
        # If there are no 1's or all are 1's, no swaps needed
        if total_ones == 0 or total_ones == n:
            return 0
        
        # Step 2: Create an extended array to handle the circular nature
        extended_nums = nums + nums
        
        # Step 3: Use sliding window to find the minimum number of 0's in any window of size total_ones
        min_zeros = float('inf')
        current_zeros = 0
        
        # Initial window setup
        for i in range(total_ones):
            if extended_nums[i] == 0:
                current_zeros += 1
        
        min_zeros = min(min_zeros, current_zeros)
        
        # Slide the window
        for i in range(1, n):
            if extended_nums[i - 1] == 0:
                current_zeros -= 1
            if extended_nums[i + total_ones - 1] == 0:
                current_zeros += 1
            min_zeros = min(min_zeros, current_zeros)
        
        return min_zeros
        
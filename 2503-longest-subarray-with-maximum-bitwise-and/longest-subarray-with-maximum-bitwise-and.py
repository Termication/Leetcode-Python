class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Step 1: Find the maximum value in the array
        max_val = max(nums)
        
        # Step 2: Find the longest subarray where all elements are equal to the maximum value
        longest = 0
        current_length = 0
        
        for num in nums:
            if num == max_val:
                current_length += 1
                longest = max(longest, current_length)
            else:
                current_length = 0  # Reset the count if the element is not equal to max_val
        
        return longest
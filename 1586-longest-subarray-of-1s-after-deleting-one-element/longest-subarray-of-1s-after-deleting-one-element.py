class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        zero_count = 0
        max_len = 0
        n = len(nums)
        
        for right in range(n):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            current_len = right - left + 1
            max_len = max(max_len, current_len - 1)
        
        return max_len


        
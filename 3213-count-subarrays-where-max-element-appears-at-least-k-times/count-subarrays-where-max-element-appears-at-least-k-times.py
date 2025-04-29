class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        n = len(nums)
        count = 0
        left = 0
        freq = 0  # Frequency of max_val in current window

        for right in range(n):
            if nums[right] == max_val:
                freq += 1
            
            while freq >= k:
                count += n - right  # all subarrays starting at left and ending from right to end are valid
                if nums[left] == max_val:
                    freq -= 1
                left += 1

        return count
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # Step 1: Sort the array
        nums.sort()
        n = len(nums)
        count = 0
        
        # Step 2: Loop through each element and use binary search to find valid pairs
        for i in range(n):
            # Calculate the range for the valid pairs
            left = lower - nums[i]
            right = upper - nums[i]
            
            # Use binary search to find the range of valid indices j > i
            start = bisect_left(nums, left, i + 1)
            end = bisect_right(nums, right, i + 1)
            
            # Count the number of valid pairs
            count += (end - start)
        
        return count
        
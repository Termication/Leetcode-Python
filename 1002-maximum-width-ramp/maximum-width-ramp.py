class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
    
        # Step 1: Build the decreasing stack of indices
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        max_width = 0
        
        # Step 2: Traverse from the end to find the maximum width ramp
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                i = stack.pop()
                max_width = max(max_width, j - i)
        
        return max_width
            
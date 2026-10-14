class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        # Step 1: Compute squares of all elements
        squares = [x * x for x in nums]
        
        # Step 2: Sort the squares in ascending order
        squares.sort()
        
        # Step 3: Split into smallest (negative) and largest (positive) groups
        num_negative = len(nums) // 2
        
        negative_sum = sum(squares[:num_negative])
        positive_sum = sum(squares[num_negative:])
        
        return positive_sum - negative_sum
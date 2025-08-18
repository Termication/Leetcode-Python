class Solution(object):
    def judgePoint24(self, cards):
        """
        :type cards: List[int]
        :rtype: bool
        """
         # Convert integers to floats to handle division
        nums = [float(card) for card in cards]
        
        def solve(nums):
            # Base case: if only one number remains
            if len(nums) == 1:
                # Check if the number is close to 24 (accounting for floating point imprecision)
                return abs(nums[0] - 24) < 1e-6
            
            # Try all possible combinations of two numbers
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    # Create a copy of the numbers list
                    new_nums = nums[:i] + nums[i+1:j] + nums[j+1:]
                    
                    # Try all possible operations
                    operations = [
                        nums[i] + nums[j],
                        nums[i] - nums[j],
                        nums[j] - nums[i],
                        nums[i] * nums[j]
                    ]
                    
                    # Add division (avoiding division by zero)
                    if abs(nums[j]) > 1e-6:
                        operations.append(nums[i] / nums[j])
                    if abs(nums[i]) > 1e-6:
                        operations.append(nums[j] / nums[i])
                    
                    # Recursively try each new combination
                    for op in operations:
                        if solve(new_nums + [op]):
                            return True
            
            return False
        
        return solve(nums)
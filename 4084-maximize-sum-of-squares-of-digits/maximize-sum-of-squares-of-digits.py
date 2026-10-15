class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # A valid number cannot have a sum greater than 9 * num or sum < 1
        if sum > 9 * num or sum < 1:
            return ""
        
        digits = []
        rem_sum = sum
        
        for _ in range(num):
            # Take the largest possible digit (up to 9)
            d = min(9, rem_sum)
            digits.append(str(d))
            rem_sum -= d
            
        return "".join(digits)
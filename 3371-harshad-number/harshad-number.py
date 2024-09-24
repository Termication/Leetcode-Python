class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        # Calculate the sum of the digits of x
        digit_sum = sum(int(digit) for digit in str(x))
        
        # Check if x is divisible by the sum of its digits
        if x % digit_sum == 0:
            return digit_sum
        else:
            return -1

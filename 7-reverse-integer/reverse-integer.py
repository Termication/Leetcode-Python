class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Check if the number is negative
        negative = x < 0
        if negative:
            x = -x

        # Reverse the integer
        reversed_x = int(str(x)[::-1])

        # Restore the sign if it was negative
        if negative:
            reversed_x = -reversed_x

        # Check for overflow
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0

        return reversed_x
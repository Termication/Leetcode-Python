class Solution:
    def myAtoi(self, s: str) -> int:
        # Define the bounds of a 32-bit signed integer
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Initialize the index and length of the string
        i = 0
        n = len(s)
        
        # Skip leading whitespaces
        while i < n and s[i].isspace():
            i += 1
        
        # Check if the string is empty after removing whitespaces
        if i >= n:
            return 0
        
        # Check for the sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        # Initialize the result number
        result = 0
        
        # Convert the characters to integer
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Check for overflow and underflow
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        return sign * result
        
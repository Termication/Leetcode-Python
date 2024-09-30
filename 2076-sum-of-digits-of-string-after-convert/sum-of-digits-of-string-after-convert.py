class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Step 1: Convert the string into the corresponding integer
        converted = ''.join(str(ord(char) - ord('a') + 1) for char in s)
        
        # Step 2: Transform the integer by summing its digits
        # Convert the string of digits to an integer and sum its digits
        total = sum(int(digit) for digit in converted)
        
        # Step 3: Repeat the transformation k - 1 times
        for _ in range(k - 1):
            total = sum(int(digit) for digit in str(total))
        
        return total
        
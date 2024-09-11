class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR the two numbers to find differing bits
        xor_result = start ^ goal
        # Count the number of 1's in the XOR result
        return bin(xor_result).count('1')
        
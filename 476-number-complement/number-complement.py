class Solution:
    def findComplement(self, num: int) -> int:
        # Create a mask with all bits set to 1 that matches the length of num's binary representation
        mask = (1 << num.bit_length()) - 1
        
        # Compute the complement using XOR operation with the mask
        complement = num ^ mask
        
        return complement
            
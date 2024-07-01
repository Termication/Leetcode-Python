class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            
            # Append the current bit (carry % 2) to the result
            result.append(str(carry % 2))
            
            # Update carry (carry // 2)
            carry //= 2
        
        # Since we've built the result in reverse order, reverse it back
        return ''.join(result[::-1])
class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def gcd(a, b):
            """Helper function to calculate GCD using the Euclidean algorithm."""
            while b:
                a, b = b, a % b
            return a

        res = []
        
        for num in nums:
            res.append(num)
            
            while len(res) >= 2:
                y = res.pop()
                x = res[-1]
                
                # Use the custom gcd function instead of math.gcd
                common_divisor = gcd(x, y)
                
                if common_divisor == 1:
                    res.append(y)
                    break
                
                res[-1] = (x * y) // common_divisor
                
        return res
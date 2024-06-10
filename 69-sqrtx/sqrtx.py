class Solution:
    def mySqrt(self, x: int) -> int:
        # If x is less than 2, return x immediately as the square root of 0 is 0 and the square root of 1 is 1.
        if x < 2:
            return x

        #The binary search will help narrow down the potential integer square roots.
        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
        
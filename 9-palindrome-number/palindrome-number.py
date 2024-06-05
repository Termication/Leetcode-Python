class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Convert the number to string to easily reverse it
        num_str = str(x)
        # Reverse the string and compare with the original string
        return num_str == num_str[::-1]
        
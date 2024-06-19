class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)  # Length of the input string
        char_map = {}  # Dictionary to store characters and their indices
        max_len = 0  # Variable to store the maximum length of substring without repeating characters
        left = 0  # Pointer for the start of the current valid substring
        
        for right in range(n):  # Iterate over each character in the string
            if s[right] in char_map and char_map[s[right]] >= left:
                # If s[right] is already in char_map and its index is within the current window [left, right]
                left = char_map[s[right]] + 1  # Move left pointer to the right of the last occurrence of s[right]
            
            char_map[s[right]] = right  # Update the index of s[right] in the char_map
            max_len = max(max_len, right - left + 1)  # Update max_len with the maximum length of current valid substring
        
        return max_len  # Return the maximum length of substring without repeating characters

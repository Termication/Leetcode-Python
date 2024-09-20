class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # If s is empty, it's already a palindrome
        if not s:
            return s
        
        # Get the reversed string
        rev_s = s[::-1]
        
        # Create the new string with a separator to avoid overlap
        new_s = s + '#' + rev_s
        
        # Compute the KMP table (partial match table)
        n = len(new_s)
        lps = [0] * n  # Longest Prefix Suffix table
        for i in range(1, n):
            j = lps[i - 1]
            while j > 0 and new_s[i] != new_s[j]:
                j = lps[j - 1]
            if new_s[i] == new_s[j]:
                j += 1
            lps[i] = j
        
        # The longest palindrome prefix length is stored in the last value of lps
        longest_palindrome_prefix_len = lps[-1]
        
        # Characters to add at the front are the ones left in rev_s after the palindrome prefix
        to_add = rev_s[:len(s) - longest_palindrome_prefix_len]
        
        # Construct the shortest palindrome
        return to_add + s
        
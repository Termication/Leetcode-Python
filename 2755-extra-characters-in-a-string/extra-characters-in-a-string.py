class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Convert the dictionary list to a set for faster lookup
        word_set = set(dictionary)
        
        # DP array initialized to a large number
        n = len(s)
        dp = [float('inf')] * (n + 1)
        
        # Base case: no extra characters if the string is empty
        dp[0] = 0
        
        # Iterate over the entire string
        for i in range(1, n + 1):
            # Check all possible substrings s[j:i]
            for j in range(i):
                # If s[j:i] is a word in the dictionary, we may be able to update dp[i]
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])
            # Also consider the case where we don't use any valid word and count character i-1 as extra
            dp[i] = min(dp[i], dp[i - 1] + 1)
        
        # The answer will be in dp[n]
        return dp[n]
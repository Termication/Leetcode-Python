class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        n = len(s)
        
        # Precompute the total number of ones
        total_ones = s.count('1')
        
        left_zeros = 0
        right_ones = total_ones
        
        for i in range(n - 1):  # Exclude last index since we need non-empty substrings
            if s[i] == '0':
                left_zeros += 1
            else:
                right_ones -= 1

            # Calculate score at this split
            score = left_zeros + right_ones
            max_score = max(max_score, score)
        
        return max_score
        
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Base case: if s1 is longer than s2, s2 cannot contain a permutation of s1
        if len(s1) > len(s2):
            return False
        
        # Frequency map for s1
        s1_count = Counter(s1)
        # Frequency map for the current window in s2
        window_count = Counter()

        # Initial window of size len(s1) - 1
        for i in range(len(s1) - 1):
            window_count[s2[i]] += 1

        # Start sliding the window over s2
        for i in range(len(s1) - 1, len(s2)):
            # Add the current character to the window
            window_count[s2[i]] += 1

            # Compare the current window with s1's character frequencies
            if window_count == s1_count:
                return True

            # Move the window forward: remove the character at the start of the window
            window_count[s2[i - len(s1) + 1]] -= 1
            # If the count of a character goes to zero, remove it from the window_count
            if window_count[s2[i - len(s1) + 1]] == 0:
                del window_count[s2[i - len(s1) + 1]]

        return False              
        
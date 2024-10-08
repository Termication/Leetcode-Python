class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)  # Convert allowed characters to a set
        consistent_count = 0

        for word in words:
            if all(char in allowed_set for char in word):  # Check if all characters in word are in allowed_set
                consistent_count += 1

        return consistent_count
            
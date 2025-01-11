class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # Count the frequency of each character
        char_count = Counter(s)
        
        # Count characters with odd frequencies
        odd_count = sum(1 for freq in char_count.values() if freq % 2 != 0)
        
        # Check if k is within the valid range
        return odd_count <= k <= len(s)

        
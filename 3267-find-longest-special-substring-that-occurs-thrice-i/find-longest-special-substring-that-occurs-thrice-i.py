class Solution:
    def maximumLength(self, s: str) -> int:
        # Helper function to check if a substring is "special"
        def is_special(substring):
            return len(set(substring)) == 1  # Only one unique character

        n = len(s)

        # Iterate over lengths of substrings from n down to 1
        for length in range(n, 0, -1):
            substring_count = {}
            
            # Generate all substrings of current length
            for i in range(n - length + 1):
                substring = s[i:i + length]
                
                # Check if the substring is special
                if is_special(substring):
                    substring_count[substring] = substring_count.get(substring, 0) + 1

            # Check if any special substring occurs at least three times
            for count in substring_count.values():
                if count >= 3:
                    return length

        # If no valid substring is found
        return -1
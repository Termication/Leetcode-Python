class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Step 1: Remove trailing spaces
        s = s.rstrip()
        
        # Step 2: Split the string by spaces
        words = s.split(' ')
        
        # Step 3: Get the last word
        last_word = words[-1]
        
        # Step 4: Return the length of the last word
        return len(last_word)
        
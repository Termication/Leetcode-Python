class Solution:
    def makeFancyString(self, s: str) -> str:
        # Initialize a list to store characters of the resulting fancy string.
        result = []
        
        # Traverse through the input string.
        for char in s:
            # Check if the last two characters in result are the same as the current character.
            # If they are, we skip adding this character to prevent three consecutive characters.
            if len(result) >= 2 and result[-1] == char and result[-2] == char:
                continue
            result.append(char)
        
        # Join the list to form the resulting string and return it.
        return ''.join(result)
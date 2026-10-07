class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Helper function to check if a string is valid
        def isValid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        # BFS initialization
        current_level = {s}
        
        while True:
            # Filter valid strings in the current level
            valid_results = [item for item in current_level if isValid(item)]
            
            # If we found valid strings at this depth, this is the minimum removal level
            if valid_results:
                return valid_results
            
            # Otherwise, generate the next level by removing one parenthesis at a time
            next_level = set()
            for item in current_level:
                for i in range(len(item)):
                    # Only remove parentheses, ignore letters
                    if item[i] in ('(', ')'):
                        next_level.add(item[:i] + item[i+1:])
            
            current_level = next_level
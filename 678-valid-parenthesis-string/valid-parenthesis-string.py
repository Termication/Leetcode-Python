class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0
        max_open = 0
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            else:  # char == '*'
                min_open -= 1
                max_open += 1
                
            # If max_open drops below 0, we have unmatched ')'
            if max_open < 0:
                return False
            
            # min_open cannot be negative; '*' can act as empty string
            min_open = max(min_open, 0)
            
        return min_open == 0
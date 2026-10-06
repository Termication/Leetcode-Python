class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left_required = 0
        right_required = 0
        
        for char in s:
            if char == '(':
                right_required += 1
            else:
                # If there is an unmatched opening bracket available, match it
                if right_required > 0:
                    right_required -= 1
                else:
                    # Otherwise, we need an opening bracket for this closing bracket
                    left_required += 1
                    
        return left_required + right_required
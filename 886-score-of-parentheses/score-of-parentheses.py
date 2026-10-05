class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  # The score at the current nesting level
        
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                v = stack.pop()
                # If v is 0, it means '()', score is 1. Otherwise, it's 2 * v.
                score = max(2 * v, 1)
                stack[-1] += score
                
        return stack[0]
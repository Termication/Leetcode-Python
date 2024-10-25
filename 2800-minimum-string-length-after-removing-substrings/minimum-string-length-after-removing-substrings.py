class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for char in s:
            # Check the stack's last character with the current character
            if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
                # Pop if the last two characters form "AB" or "CD"
                stack.pop()
            else:
                # Otherwise, push the current character
                stack.append(char)
        
        # The length of the remaining stack is the minimum possible length
        return len(stack)
            
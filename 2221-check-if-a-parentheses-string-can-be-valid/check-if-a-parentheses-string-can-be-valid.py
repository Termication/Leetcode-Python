class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False  # Odd length strings can't be valid
        
        n = len(s)
        open_count, close_count = 0, 0  # Balance counts
        unlock_left = 0  # Count of unlocked positions
        
        # Left-to-right pass
        for i in range(n):
            if locked[i] == '0':  # Unlocked position
                unlock_left += 1
            elif s[i] == '(':
                open_count += 1
            else:
                close_count += 1
            
            # Check balance
            if close_count > open_count + unlock_left:
                return False  # Too many ')' to balance
        
        # Reset counts for right-to-left pass
        open_count, close_count = 0, 0
        unlock_right = 0
        
        # Right-to-left pass
        for i in range(n - 1, -1, -1):
            if locked[i] == '0':  # Unlocked position
                unlock_right += 1
            elif s[i] == ')':
                close_count += 1
            else:
                open_count += 1
            
            # Check balance
            if open_count > close_count + unlock_right:
                return False  # Too many '(' to balance
        
        return True
            
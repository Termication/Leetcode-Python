class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Remove all blanks and check if the sequence of pieces matches
        if start.replace('_', '') != target.replace('_', ''):
            return False
        
        # Pointers to iterate through `start` and `target`
        i, j = 0, 0
        n = len(start)
        
        while i < n and j < n:
            # Skip blanks in both strings
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1
            
            # If both pointers are within bounds, check movement constraints
            if i < n and j < n:
                if start[i] != target[j]:
                    return False
                if start[i] == 'L' and i < j:  # 'L' cannot move right
                    return False
                if start[i] == 'R' and i > j:  # 'R' cannot move left
                    return False
            
            # Move to the next characters
            i += 1
            j += 1
        
        return True
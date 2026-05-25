from collections import deque

class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        n = len(s)
        q = deque([0])
        farthest = 0  # track the furthest index we’ve processed
        
        while q:
            i = q.popleft()
            if i == n - 1:
                return True
            
            # Explore new range [i+minJump, i+maxJump]
            start = max(i + minJump, farthest + 1)
            end = min(i + maxJump, n - 1)
            
            for j in range(start, end + 1):
                if s[j] == '0':
                    q.append(j)
            
            farthest = end  # update processed boundary
        
        return False

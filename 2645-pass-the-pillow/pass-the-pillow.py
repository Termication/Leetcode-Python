class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # Calculate the effective position in a complete cycle
        cycle_time = time % (2 * (n - 1))
        
        # Determine if the pillow is moving forward or backward
        if cycle_time < n:
            return cycle_time + 1
        else:
            return 2 * n - cycle_time - 1
        
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # Step 1: Calculate the total chalk required for one full round
        total_chalk = sum(chalk)
        
        # Step 2: Use modulo to reduce k to within one cycle
        k %= total_chalk
        
        # Step 3: Find the student who will run out of chalk
        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            k -= chalk[i]
        
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Edge case: If no items are needed
        if need1 <= 0 and need2 <= 0:
            return 0
            
        need1 = max(0, need1)
        need2 = max(0, need2)
        
        # Option 1: Buy individual items for all requirements
        ans1 = need1 * cost1 + need2 * cost2
        
        # Option 2: Buy type 3 items to cover min(need1, need2)
        shared = min(need1, need2)
        ans2 = shared * costBoth + (need1 - shared) * cost1 + (need2 - shared) * cost2
        
        # Option 3: Buy type 3 items to cover max(need1, need2)
        max_needed = max(need1, need2)
        ans3 = max_needed * costBoth
        
        return min(ans1, ans2, ans3)
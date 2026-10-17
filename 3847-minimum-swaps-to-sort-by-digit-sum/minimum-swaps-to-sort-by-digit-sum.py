class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Helper function to compute digit sum
        def get_digit_sum(val: int) -> int:
            return sum(int(d) for d in str(val))
        
        # Step 1: Pair each element with its digit sum and original index
        # Format: (digit_sum, value, original_index)
        indexed_nums = [(get_digit_sum(val), val, i) for i, val in enumerate(nums)]
        
        # Step 2: Sort according to the specified rule
        sorted_nums = sorted(indexed_nums)
        
        # Step 3: Find permutation cycles
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            # Skip if already visited or already in correct position
            if visited[i] or sorted_nums[i][2] == i:
                visited[i] = True
                continue
            
            # Trace the cycle
            cycle_size = 0
            curr = i
            
            while not visited[curr]:
                visited[curr] = True
                # Move to the index where nums[curr] originally came from
                curr = sorted_nums[curr][2]
                cycle_size += 1
                
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        return swaps
class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Count frequency of set bits at each position (up to 30 bits)
        bit_counts = [0] * 30
        for num in nums:
            for bit in range(30):
                if (num >> bit) & 1:
                    bit_counts[bit] += 1
                    
        # Step 2: Construct the k largest elements greedily
        total_sum_of_squares = 0
        
        for _ in range(k):
            val = 0
            for bit in range(30):
                if bit_counts[bit] > 0:
                    val |= (1 << bit)
                    bit_counts[bit] -= 1
                    
            total_sum_of_squares = (total_sum_of_squares + val * val) % MOD
            
        return total_sum_of_squares
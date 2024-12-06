class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)  # Use a set for fast lookup
        current_sum = 0
        count = 0
        
        # Iterate through integers in range [1, n]
        for num in range(1, n + 1):
            if num in banned_set:
                continue  # Skip banned numbers
            if current_sum + num > maxSum:
                break  # Stop if adding this number exceeds maxSum
            current_sum += num
            count += 1  # Increment the count of chosen integers
        
        return count
            
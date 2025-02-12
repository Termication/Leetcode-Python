from collections import defaultdict
from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n = n // 10
            return s
        
        digit_sum_map = defaultdict(list)
        for num in nums:
            s = digit_sum(num)
            digit_sum_map[s].append(num)
        
        max_sum = -1
        for key in digit_sum_map:
            numbers = digit_sum_map[key]
            if len(numbers) >= 2:
                sorted_numbers = sorted(numbers, reverse=True)
                current_sum = sorted_numbers[0] + sorted_numbers[1]
                if current_sum > max_sum:
                    max_sum = current_sum
        
        return max_sum
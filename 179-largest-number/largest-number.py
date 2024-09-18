from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert numbers to strings
        nums = list(map(str, nums))
        
        # Custom comparator: if x + y > y + x, x should come before y
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # Sort the numbers with the custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Join the sorted list into a single string
        largest_num = ''.join(nums)
        
        # Handle the case where the numbers are all zeros
        return '0' if largest_num[0] == '0' else largest_num
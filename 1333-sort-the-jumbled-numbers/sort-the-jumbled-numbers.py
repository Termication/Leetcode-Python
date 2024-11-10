class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapped_value(num):
            # Convert each digit of num using the mapping array
            return int("".join(str(mapping[int(d)]) for d in str(num)))
        
        # Sort nums based on the mapped value, using a stable sort
        return sorted(nums, key=mapped_value)
            
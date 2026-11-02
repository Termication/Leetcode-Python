class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_val = min(nums)
        moves = 0
        for num in nums:
            moves += num - min_val
        return moves
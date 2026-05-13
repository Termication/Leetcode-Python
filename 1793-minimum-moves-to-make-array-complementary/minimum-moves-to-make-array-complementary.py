class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        n = len(nums)
        diff = [0] * (2*limit + 2)

        for i in range(n//2):
            a, b = nums[i], nums[n-1-i]
            low = min(a, b) + 1
            high = max(a, b) + limit
            s = a + b

            # Default: 2 moves for all sums
            diff[2] += 2
            diff[low] -= 1
            diff[s] -= 1
            diff[s+1] += 1
            diff[high+1] += 1

        res = float('inf')
        cur = 0
        for t in range(2, 2*limit+1):
            cur += diff[t]
            res = min(res, cur)

        return res

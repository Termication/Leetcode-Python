class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        pairs = sorted((x, i) for i, x in enumerate(nums))

        groups = []
        cur = [pairs[0]]

        for i in range(1, n):
            if pairs[i][0] - pairs[i - 1][0] <= limit:
                cur.append(pairs[i])
            else:
                groups.append(cur)
                cur = [pairs[i]]

        groups.append(cur)

        ans = nums[:]

        for group in groups:
            indices = sorted(idx for _, idx in group)
            values = sorted(val for val, _ in group)

            for idx, val in zip(indices, values):
                ans[idx] = val

        return ans
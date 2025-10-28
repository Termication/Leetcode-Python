class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        pref = 0
        ans = 0
        for x in nums:
            if x == 0:
                diff = abs(2*pref - total)  # |L - R| where L=pref, R=total-L
                if diff == 0:
                    ans += 2
                elif diff == 1:
                    ans += 1
            pref += x
        return ans
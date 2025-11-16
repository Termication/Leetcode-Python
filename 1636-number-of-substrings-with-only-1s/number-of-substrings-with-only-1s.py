MOD = 10**9 + 7

class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        cur = 0  # current run length of '1'
        for ch in s:
            if ch == '1':
                cur += 1
            else:
                if cur:
                    res = (res + cur * (cur + 1) // 2) % MOD
                    cur = 0
        if cur:
            res = (res + cur * (cur + 1) // 2) % MOD
        return res
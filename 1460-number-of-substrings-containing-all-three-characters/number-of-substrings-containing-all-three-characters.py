class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = [-1, -1, -1]  # positions of a, b, c
        res = 0
        for i, ch in enumerate(s):
            last[ord(ch) - ord('a')] = i
            if -1 not in last:  # all seen
                res += 1 + min(last)
        return res

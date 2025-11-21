class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        first = [-1] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i

        ans = 0
        for outer in range(26):
            l = first[outer]
            r = last[outer]
            if l == -1 or l >= r:
                continue
            seen_mid = [False] * 26
            for k in range(l + 1, r):
                seen_mid[ord(s[k]) - 97] = True
            ans += sum(seen_mid)
        return ans
class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Map letters to coordinates
        def pos(c):
            idx = ord(c) - ord('A')
            return divmod(idx, 6)  # (row, col)

        def dist(a, b):
            ax, ay = pos(a)
            bx, by = pos(b)
            return abs(ax - bx) + abs(ay - by)

        n = len(word)
        # dp[i][j] = min cost to type up to i, with other finger at letter j
        # j is 0..25 (letter index), or -1 meaning unused
        from collections import defaultdict
        dp = { -1: 0 }  # initially no other finger used

        for i in range(1, n):
            ndp = defaultdict(lambda: float('inf'))
            for j in dp:
                cost = dp[j]
                # Option 1: use same finger as previous (other finger unchanged)
                ndp[j] = min(ndp[j], cost + dist(word[i-1], word[i]))
                # Option 2: use other finger to press word[i]
                if j == -1:
                    ndp[ord(word[i-1]) - ord('A')] = min(ndp[ord(word[i-1]) - ord('A')], cost)
                else:
                    ndp[ord(word[i-1]) - ord('A')] = min(ndp[ord(word[i-1]) - ord('A')],
                                                         cost + dist(chr(j + ord('A')), word[i]))
            dp = ndp

        return min(dp.values())

class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        ans = 0
        prev = 0
        for row in bank:
            cnt = row.count('1')
            if cnt:
                ans += prev * cnt
                prev = cnt
        return ans
            
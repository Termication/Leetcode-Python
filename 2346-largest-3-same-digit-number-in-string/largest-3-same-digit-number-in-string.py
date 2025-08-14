class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        best = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                triple = num[i] * 3
                if triple > best:      # lexicographic works since all    candidates have length 3
                    best = triple
        return best
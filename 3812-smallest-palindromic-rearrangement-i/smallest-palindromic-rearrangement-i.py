class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        
        freq = Counter(s)
        left_half = []
        middle = ""
        
        for ch in sorted(freq.keys()):
            count = freq[ch]
            left_half.append(ch * (count // 2))
            if count % 2 == 1 and middle == "":
                middle = ch  # pick smallest odd char
        
        left = "".join(left_half)
        right = left[::-1]
        return left + middle + right

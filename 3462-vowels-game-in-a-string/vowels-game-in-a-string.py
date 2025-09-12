class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_count = 0
        
        for char in s:
            if char in vowels:
                vowel_count += 1
                
        # Alice loses if and only if she cannot make a move on her first turn,
        # which happens only when there are no vowels.
        if vowel_count == 0:
            return False
        
        # If there is at least one vowel, Alice has a guaranteed winning strategy.
        return True

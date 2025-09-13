from collections import Counter

class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1. Define vowels and count all character frequencies
        vowels = {'a', 'e', 'i', 'o', 'u'}
        char_counts = Counter(s)
        
        # 2. Initialize max frequencies to 0
        max_vowel_freq = 0
        max_consonant_freq = 0
        
        # 3. Iterate through the character counts
        for char, freq in char_counts.items():
            if char in vowels:
                # It's a vowel, update the max vowel frequency
                if freq > max_vowel_freq:
                    max_vowel_freq = freq
            else:
                # It's a consonant, update the max consonant frequency
                if freq > max_consonant_freq:
                    max_consonant_freq = freq
                    
        # 4. Return the sum
        return max_vowel_freq + max_consonant_freq
        
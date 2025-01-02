class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(words)

        # Step 1: Create a prefix sum array for vowel strings
        prefix_vowel_count = [0] * (n + 1)
        
        for i, word in enumerate(words):
            # Check if the word starts and ends with a vowel
            if word[0] in vowels and word[-1] in vowels:
                prefix_vowel_count[i + 1] = prefix_vowel_count[i] + 1
            else:
                prefix_vowel_count[i + 1] = prefix_vowel_count[i]

        # Step 2: Answer the queries using the prefix sum array
        result = []
        for li, ri in queries:
            # Count of vowel strings in range [li, ri]
            result.append(prefix_vowel_count[ri + 1] - prefix_vowel_count[li])
        
        return result
            
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Calculate the maximum frequency of each character in words2
        max_freq = Counter()
        for word in words2:
            word_count = Counter(word)
            for char, freq in word_count.items():
                max_freq[char] = max(max_freq[char], freq)
        
        # Function to check if a word satisfies the max_freq condition
        def is_universal(word):
            word_count = Counter(word)
            for char, freq in max_freq.items():
                if word_count[char] < freq:
                    return False
            return True

        # Filter words1 for universal words
        result = [word for word in words1 if is_universal(word)]
        return result
        
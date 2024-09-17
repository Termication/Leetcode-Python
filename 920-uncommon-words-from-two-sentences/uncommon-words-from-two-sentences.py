from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split both sentences into words
        words_s1 = s1.split()
        words_s2 = s2.split()

        # Count frequencies of all words in both sentences
        word_count = Counter(words_s1 + words_s2)

        # Return words that appear exactly once
        return [word for word, count in word_count.items() if count == 1]
            
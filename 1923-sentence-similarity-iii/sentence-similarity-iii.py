class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Split sentences into lists of words
        words1 = sentence1.split()
        words2 = sentence2.split()

        # Initialize two pointers for matching words from both ends
        start = 0
        end = 0

        # Match words from the beginning
        while start < len(words1) and start < len(words2) and words1[start] == words2[start]:
            start += 1

        # Match words from the end
        while end < len(words1) - start and end < len(words2) - start and words1[-(end + 1)] == words2[-(end + 1)]:
            end += 1

        # Check if the total matched words cover the shorter sentence
        return start + end >= min(len(words1), len(words2))
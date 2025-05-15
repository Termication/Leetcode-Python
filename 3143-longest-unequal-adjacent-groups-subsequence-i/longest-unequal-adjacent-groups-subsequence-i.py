class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result_subsequence = []
        # Track the group of the last word added to the subsequence.
        # Initialize to a value not in [0, 1] to ensure the first word is added.
        last_group = -1

        for i in range(len(words)):
            current_word = words[i]
            current_group = groups[i]

            # Add the word if it's the first one or its group differs from the last added.
            if not result_subsequence or current_group != last_group:
                result_subsequence.append(current_word)
                last_group = current_group

        return result_subsequence
        
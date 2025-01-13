class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """
        Finds all strings in a list that are substrings of other strings in the list.

        Args:
            words: A list of strings.

        Returns:
            A list of strings that are substrings of other strings in the input list.
        """
        result = []
        n = len(words)

        for i in range(n):
            for j in range(n):
                if i != j and words[i] in words[j]:  # Check if words[i] is a substring of words[j]
                    result.append(words[i])
                    break  # Once a string is found as a substring, no need to check further

        return list(set(result)) #remove duplicates and convert back to list

        
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        """
        Finds the index (1-indexed) of the first word in the sentence where
        searchWord is a prefix. Returns -1 if no such word exists.

        Args:
            sentence (str): A string consisting of words separated by a single space.
            searchWord (str): The word to search for as a prefix.

        Returns:
            int: Index of the first word where searchWord is a prefix, or -1.
        """
        words = sentence.split()  # Split the sentence into words.
        
        for idx, word in enumerate(words):
            if word.startswith(searchWord):  # Check if searchWord is a prefix of the word.
                return idx + 1  # Return 1-indexed position.
        
        return -1  # Return -1 if no match is found.
        
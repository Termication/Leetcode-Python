class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Split the sentence into words
        words = sentence.split()
        
        # Iterate through each word, checking the circular condition
        for i in range(len(words)):
            # Get the last character of the current word
            last_char = words[i][-1]
            # Get the first character of the next word (circular with modulo)
            first_char_next = words[(i + 1) % len(words)][0]
            
            # If the last character of the current word does not match the first character of the next word
            if last_char != first_char_next:
                return False
        
        # If all conditions are met, return True
        return True
            
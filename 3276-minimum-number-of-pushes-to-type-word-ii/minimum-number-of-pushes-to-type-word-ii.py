class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import Counter

        # Count the frequency of each letter in the word
        frequency = Counter(word)

        # Sort the letters by frequency in descending order
        sorted_letters = sorted(frequency.items(), key=lambda x: -x[1])
        
        # Initialize the keypress count
        keypress_count = 0
        
        # We have 8 keys: 2 to 9
        key_capacity = [0] * 8  # Represents the number of letters each key can hold initially
        
        # Iterate over each letter and its frequency
        for letter, freq in sorted_letters:
            # Find the key with the current minimum capacity (i.e., least letters assigned)
            min_key = key_capacity.index(min(key_capacity))
            
            # Calculate key presses for this letter
            presses = key_capacity[min_key] + 1
            keypress_count += presses * freq
            
            # Update the capacity of the chosen key
            key_capacity[min_key] += 1
        
        return keypress_count
        
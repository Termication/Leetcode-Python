from collections import Counter
import heapq


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        """
        Constructs the lexicographically largest string under repeatLimit constraints.

        Args:
            s (str): Input string.
            repeatLimit (int): Maximum consecutive occurrences of any character.

        Returns:
            str: Lexicographically largest valid string.
        """
        # Count the frequencies of each character
        freq = Counter(s)
        # Max-heap: store characters and their frequencies (-ord for max heap)
        heap = [(-ord(char), count) for char, count in freq.items()]
        heapq.heapify(heap)
        
        result = []
        
        while heap:
            # Get the largest available character
            char_neg, count = heapq.heappop(heap)
            char = chr(-char_neg)
            
            # Determine how many times we can add this character
            add_count = min(count, repeatLimit)
            result.append(char * add_count)
            count -= add_count
            
            # If there is still remaining frequency for this character
            if count > 0:
                # Try to add the next largest character
                if not heap:
                    break  # No other characters to use, stop
                
                # Get the next largest character
                next_char_neg, next_count = heapq.heappop(heap)
                next_char = chr(-next_char_neg)
                
                # Add one occurrence of the next largest character
                result.append(next_char)
                next_count -= 1
                
                # Push back both characters into the heap (if any remain)
                if next_count > 0:
                    heapq.heappush(heap, (next_char_neg, next_count))
                heapq.heappush(heap, (char_neg, count))
        
        return ''.join(result)
            
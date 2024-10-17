class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of characters for easy manipulation
        num_list = list(str(num))

        # Record the last occurrence of each digit
        last = {int(x): i for i, x in enumerate(num_list)}

        # Traverse the number's digits
        for i, digit in enumerate(num_list):
            # Check for a higher digit that can be swapped
            for d in range(9, int(digit), -1):
                if last.get(d, -1) > i:
                    # Perform the swap
                    num_list[i], num_list[last[d]] = num_list[last[d]], num_list[i]
                    # Return the new number after the swap
                    return int(''.join(num_list))

        # If no swap was made, return the original number
        return num
            
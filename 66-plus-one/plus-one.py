class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Traverse the list from the end to the beginning
        for i in range(len(digits) - 1, -1, -1):
            # Add one to the current digit
            digits[i] += 1
            # If the digit becomes 10, set it to 0 and continue to the next digit
            if digits[i] == 10:
                digits[i] = 0
            else:
            # If no carry is needed, we can return the result immediately
                return digits
        
        # If we finished the loop and all digits were 9, we need to add a leading 1
        return [1] + digits
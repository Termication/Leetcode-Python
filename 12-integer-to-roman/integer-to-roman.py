class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the lookup table for integer to Roman numeral conversion
        value_to_symbol = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        # Initialize the result string
        result = []
        
        # Iterate through the lookup table
        for value, symbol in value_to_symbol:
            # Determine how many times the symbol fits into num
            count = num // value
            if count:
                result.append(symbol * count)  # Append the symbol count times
                num -= value * count           # Reduce num by the equivalent value
        
        # Join the list into a single string and return
        return ''.join(result)

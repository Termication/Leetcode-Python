class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        unique_nums = set()
        n = len(digits)
        
        # Pick the 1st digit (hundreds place)
        for i in range(n):
            # Pick the 2nd digit (tens place)
            for j in range(n):
                # Pick the 3rd digit (units place)
                for k in range(n):
                    
                    # Rule 1: We must use three distinct elements from the array
                    if i != j and i != k and j != k:
                        
                        # Rule 2: No leading zero (digits[i] != 0)
                        # Rule 3: Must be an even number (digits[k] % 2 == 0)
                        if digits[i] != 0 and digits[k] % 2 == 0:
                            
                            # Construct the actual number
                            num = (digits[i] * 100) + (digits[j] * 10) + digits[k]
                            
                            # Add to our set 
                            unique_nums.add(num)
                            
        return len(unique_nums)
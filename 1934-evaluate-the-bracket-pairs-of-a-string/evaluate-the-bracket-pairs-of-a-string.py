class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Step 1: Convert knowledge into a dictionary for instant O(1) lookups
        k_map = dict(knowledge)
        
        res = []
        curr_key = []
        in_bracket = False
        
        # Step 2: Iterate through s character by character
        for char in s:
            if char == '(':
                in_bracket = True
                curr_key = []  # Reset key collector
            elif char == ')':
                in_bracket = False
                key_str = "".join(curr_key)
                # Look up the key; default to '?' if it doesn't exist
                res.append(k_map.get(key_str, '?'))
            else:
                if in_bracket:
                    curr_key.append(char)
                else:
                    res.append(char)
                    
        return "".join(res)
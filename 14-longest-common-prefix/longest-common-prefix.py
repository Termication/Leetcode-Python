class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string in the array as the prefix
        prefix = strs[0]
        
        # Iterate through each string in the array
        for string in strs[1:]:
            # Compare the prefix with the current string
            while string[:len(prefix)] != prefix:
                # Reduce the prefix by one character at a time
                prefix = prefix[:len(prefix)-1]
                # If prefix becomes empty, return empty string
                if not prefix:
                    return ""
        
        return prefix
            
        
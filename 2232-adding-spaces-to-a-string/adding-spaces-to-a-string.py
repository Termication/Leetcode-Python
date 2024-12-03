class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        prev_index = 0

        for space in spaces:
            # Append the substring before the current space index
            result.append(s[prev_index:space])
            # Add the space
            result.append(" ")
            # Move the pointer forward
            prev_index = space

        # Add the remaining part of the string
        result.append(s[prev_index:])

        return "".join(result)
            
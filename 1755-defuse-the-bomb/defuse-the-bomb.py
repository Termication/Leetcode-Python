class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n

        # Create an extended version of the code for easy circular access
        extended_code = code * 2
        result = [0] * n

        if k > 0:
            # Sum the next k elements for each index
            for i in range(n):
                result[i] = sum(extended_code[i + 1:i + k + 1])
        else:
            # Sum the previous |k| elements for each index
            for i in range(n):
                result[i] = sum(extended_code[i + n + k:i + n])

        return result
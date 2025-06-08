class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        curr = 1

        for _ in range(n):
            result.append(curr)

            # Try to go deeper (e.g., from 1 to 10, 11, etc.)
            if curr * 10 <= n:
                curr *= 10
            # If we cannot go deeper
            else:
                # If we are at the largest number in the current branch or the last digit is 9
                # (e.g., from 19, or from 13 when n=13)
                if curr == n or curr % 10 == 9:
                    # Go up the tree until we find a parent whose next sibling is valid
                    # (e.g., from 19, go up to 1, then next sibling of 1 is 2)
                    while curr % 10 == 9 or curr + 1 > n:
                        curr //= 10
                    curr += 1
                # Otherwise, just go to the next sibling (e.g., from 1 to 2, or 10 to 11)
                else:
                    curr += 1
        
        return result
        
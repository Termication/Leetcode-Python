class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        curr = 1  # Start with the first number in lexicographical order
        k -= 1    # Convert k to 0-indexed for easier calculations

        while k > 0:
            # Calculate the number of elements in the current prefix's subtree
            # This is essentially counting how many numbers start with 'curr'
            # (or are 'curr' itself) up to 'n'.
            count = 0
            first = curr
            last = curr + 1 # Represents the start of the next prefix (e.g., if curr is 1, next is 2)

            while first <= n:
                # Add the numbers from 'first' up to 'min(n + 1, last) - 1'
                # min(n + 1, last) ensures we don't go beyond n.
                # Example: if curr=1, first=1, last=2. min(n+1, 2) is 2. count += 2 - 1 = 1 (for '1')
                # Next: first=10, last=20. min(n+1, 20) is 14. count += 14 - 10 = 4 (for 10,11,12,13)
                count += min(n + 1, last) - first
                first *= 10
                last *= 10

            if k >= count:
                # The k-th number is not in the current prefix's subtree.
                # Move to the next sibling prefix.
                k -= count
                curr += 1
            else:
                # The k-th number is within the current prefix's subtree.
                # Go one level deeper (append a '0').
                k -= 1 # Account for 'curr' itself
                curr *= 10
        
        return curr
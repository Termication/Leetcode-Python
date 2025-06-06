class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        n = len(s)
        if n == 0:
            return ""

        # Step 1: Precompute min_suffix array
        min_suffix = [''] * n
        min_suffix[n - 1] = s[n - 1]
        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(s[i], min_suffix[i + 1])

        result_paper = []
        temp_stack = []  # Simulates string t

        s_ptr = 0

        # Step 3: Greedy Decisions
        while s_ptr < n or temp_stack:
            # If temp_stack is empty, we must move from s to t
            if not temp_stack:
                temp_stack.append(s[s_ptr])
                s_ptr += 1
            else:
                # We have characters in temp_stack and potentially in s
                # Compare temp_stack[-1] with the smallest character remaining in s
                # If s_ptr reaches n, it means all characters from s have been moved to t
                
                if s_ptr < n and temp_stack[-1] > min_suffix[s_ptr]:
                    # There's a smaller character available in the remaining s
                    # So, we should move from s to t
                    temp_stack.append(s[s_ptr])
                    s_ptr += 1
                else:
                    # temp_stack[-1] is <= min_suffix[s_ptr] (or s_ptr == n)
                    # This means temp_stack[-1] is the smallest character we can output right now
                    # (or there are no smaller characters in s to wait for).
                    # So, pop from temp_stack and append to result_paper
                    result_paper.append(temp_stack.pop())
        
        # Step 4 & 5: All characters processed, return the joined string
        return "".join(result_paper)
        
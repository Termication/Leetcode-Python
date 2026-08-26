class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""

        for i in range(n):
            ones = 0
            for j in range(i, n):
                if s[j] == '1':
                    ones += 1

                if ones == k:
                    cur = s[i:j + 1]

                    if (ans == "" or
                        len(cur) < len(ans) or
                        (len(cur) == len(ans) and cur < ans)):
                        ans = cur

                elif ones > k:
                    break

        return ans
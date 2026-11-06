from collections import defaultdict
from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        result = [0] * len(queries)

        counts = defaultdict(int)  # server_id -> number of requests in window
        left = right = 0
        active = 0                 # distinct servers in window

        for i in order:
            q = queries[i]
            low, high = q - x, q

            # Add logs with time <= q
            while right < len(logs) and logs[right][1] <= high:
                sid = logs[right][0]
                if counts[sid] == 0:
                    active += 1
                counts[sid] += 1
                right += 1

            # Remove logs with time < q - x
            while left < right and logs[left][1] < low:
                sid = logs[left][0]
                counts[sid] -= 1
                if counts[sid] == 0:
                    active -= 1
                left += 1

            result[i] = n - active

        return result
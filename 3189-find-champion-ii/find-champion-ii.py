class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Initialize in-degree array
        in_degree = [0] * n

        # Step 2: Calculate in-degrees for each team
        for u, v in edges:
            in_degree[v] += 1

        # Step 3: Find teams with no incoming edges
        champions = [i for i in range(n) if in_degree[i] == 0]

        # Step 4: Return the result based on the number of champions
        if len(champions) == 1:
            return champions[0]  # Unique champion
        else:
            return -1  # No unique champion
            
from collections import Counter

class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        n = len(source)

        # Union-Find (Disjoint Set Union)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        # Build connected components
        for a, b in allowedSwaps:
            union(a, b)

        # Group indices by root
        groups = {}
        for i in range(n):
            root = find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(i)

        # Calculate mismatches
        mismatches = 0
        for comp in groups.values():
            src_vals = Counter(source[i] for i in comp)
            tgt_vals = Counter(target[i] for i in comp)

            # Count matches
            for val in src_vals:
                matches = min(src_vals[val], tgt_vals[val])
                src_vals[val] -= matches
                tgt_vals[val] -= matches

            mismatches += sum(src_vals.values())

        return mismatches


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Build the adjacency list for the tree
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Initialize the count of valid components
        component_count = 0

        # Helper function for DFS
        def dfs(node, parent):
            nonlocal component_count
            # Calculate the sum of the current subtree
            subtree_sum = values[node]

            for neighbor in graph[node]:
                if neighbor != parent:
                    # Recursively compute subtree sums
                    subtree_sum += dfs(neighbor, node)

            # Check if the subtree can form a valid component
            if subtree_sum % k == 0:
                component_count += 1
                return 0  # Reset sum after forming a component
            
            return subtree_sum

        # Start DFS from node 0
        dfs(0, -1)
        return component_count
        
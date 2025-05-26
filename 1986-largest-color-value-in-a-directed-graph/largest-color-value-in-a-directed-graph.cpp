#include <vector>
#include <string>
#include <queue>
#include <algorithm> // Required for std::max

class Solution {
public:
    int largestPathValue(std::string colors, std::vector<std::vector<int>>& edges) {
        int n = colors.length();

        // 1. Build Adjacency List and Calculate In-degrees
        std::vector<std::vector<int>> adj(n);
        std::vector<int> in_degree(n, 0);

        for (const auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            adj[u].push_back(v);
            in_degree[v]++;
        }

        // 2. Initialize DP Table
        // dp[i][j] stores the maximum count of character ('a' + j)
        // on a path ending at node i.
        std::vector<std::vector<int>> dp(n, std::vector<int>(26, 0));

        // 3. Initialize Queue for Kahn's Algorithm (Topological Sort)
        std::queue<int> q;
        for (int i = 0; i < n; ++i) {
            if (in_degree[i] == 0) {
                q.push(i);
            }
        }

        int nodes_visited_count = 0;
        int max_color_value = 0;

        // 4. Topological Sort and DP Update
        while (!q.empty()) {
            int u = q.front();
            q.pop();

            nodes_visited_count++;

            // Increment the count for the color of the current node 'u' itself.
            // This is done after inheriting values from predecessors, ensuring 'u' itself is counted.
            dp[u][colors[u] - 'a']++;

            // Update the global maximum color value seen so far.
            // This takes the maximum from any color count on any path ending at 'u'.
            for (int color_idx = 0; color_idx < 26; ++color_idx) {
                max_color_value = std::max(max_color_value, dp[u][color_idx]);
            }
            
            // Propagate DP values to neighbors
            for (int v : adj[u]) {
                for (int color_idx = 0; color_idx < 26; ++color_idx) {
                    // Update dp[v][color_idx] by taking the maximum from dp[u][color_idx].
                    // This means a path ending at 'v' that passes through 'u' can have
                    // at most dp[u][color_idx] of that color.
                    dp[v][color_idx] = std::max(dp[v][color_idx], dp[u][color_idx]);
                }
                in_degree[v]--;
                if (in_degree[v] == 0) {
                    q.push(v);
                }
            }
        }

        // 5. Cycle Check
        // If the number of nodes processed is less than the total number of nodes,
        // it means there's a cycle in the graph.
        if (nodes_visited_count < n) {
            return -1; 
        }

        // 6. Return the largest color value found.
        return max_color_value;
    }
};
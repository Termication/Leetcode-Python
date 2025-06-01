class Solution(object):
    def distributeCandies(self, n, limit):
        # Helper function for C(n, k)
        # Using math.comb is usually the most robust for competitive programming
        # but for C(X, 2) we can also use the direct formula (X * (X-1)) // 2
        def combinations_choose_2(val):
            if val < 2:
                return 0
            return (val * (val - 1)) // 2
            
        # Function to calculate ways to distribute `candies` among 3 children without upper limit
        # This is equivalent to C(candies + 3 - 1, 3 - 1) = C(candies + 2, 2)
        def ways_no_limit(candies_left):
            if candies_left < 0:
                return 0
            # N = candies_left, K = 3
            # So, C(N + K - 1, K - 1) = C(candies_left + 2, 2)
            return combinations_choose_2(candies_left + 2)

        L = limit + 1 # Represents the threshold for a child exceeding the limit

        # Total ways without any limit
        term_total = ways_no_limit(n)

        # Ways where at least one child exceeds the limit
        # For child 1 exceeding: n - L candies remaining
        # For child 2 exceeding: n - L candies remaining
        # For child 3 exceeding: n - L candies remaining
        term_one_exceeds = 3 * ways_no_limit(n - L)

        # Ways where at least two children exceed the limit
        # For child 1 and 2 exceeding: n - 2L candies remaining
        # For child 1 and 3 exceeding: n - 2L candies remaining
        # For child 2 and 3 exceeding: n - 2L candies remaining
        term_two_exceeds = 3 * ways_no_limit(n - 2 * L)

        # Ways where all three children exceed the limit
        # For child 1, 2, and 3 exceeding: n - 3L candies remaining
        term_three_exceeds = 1 * ways_no_limit(n - 3 * L)

        # Apply Principle of Inclusion-Exclusion
        result = term_total - term_one_exceeds + term_two_exceeds - term_three_exceeds
        
        return result
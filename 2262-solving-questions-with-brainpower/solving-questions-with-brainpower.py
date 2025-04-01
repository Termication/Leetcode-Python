class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        # dp[i] represents the maximum points that can be earned starting from question i
        dp = [0] * (n + 1)

        # Iterate through the questions in reverse order
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            # Option 1: Skip the current question
            skip = dp[i + 1]
            # Option 2: Solve the current question
            # Calculate the index of the next question that can be solved
            next_question = min(i + brainpower + 1, n)
            solve = points + dp[next_question]
            # Choose the option that yields the maximum points
            dp[i] = max(skip, solve)

        # dp[0] represents the maximum points that can be earned starting from the first question
        return dp[0]
        
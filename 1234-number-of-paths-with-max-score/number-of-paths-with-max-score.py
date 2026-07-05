class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        n = len(board)
        
        # dp[i][j] = (max_score, num_paths)
        dp = [[(-1, 0) for _ in range(n+1)] for _ in range(n+1)]
        dp[n-1][n-1] = (0, 1)  # start at 'S'
        
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] == 'X': 
                    continue
                if i == n-1 and j == n-1: 
                    continue  # skip 'S'
                
                best_score = -1
                ways = 0
                for di, dj in [(1,0),(0,1),(1,1)]:
                    ni, nj = i+di, j+dj
                    if ni < n and nj < n and dp[ni][nj][0] != -1:
                        score, cnt = dp[ni][nj]
                        if score > best_score:
                            best_score = score
                            ways = cnt
                        elif score == best_score:
                            ways = (ways + cnt) % MOD
                
                if best_score == -1:
                    continue
                
                val = 0 if board[i][j] in "SE" else int(board[i][j])
                dp[i][j] = (best_score + val, ways % MOD)
        
        return [max(dp[0][0][0],0), dp[0][0][1] % MOD]

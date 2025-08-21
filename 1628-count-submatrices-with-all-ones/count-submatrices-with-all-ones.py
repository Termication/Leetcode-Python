class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        if not mat or not mat[0]:
            return 0

        m, n = len(mat), len(mat[0])
        heights = [0] * n
        ans = 0

        for i in range(m):
            # Build histogram heights for this row
            for j in range(n):
                heights[j] = heights[j] + 1 if mat[i][j] == 1 else 0

            # Monotonic stack: (height, width_count)
            stack = []
            sum_row = 0  # total submatrices ending at this row up to current column
            for h in heights:
                cnt = 1
                while stack and stack[-1][0] >= h:
                    prev_h, prev_cnt = stack.pop()
                    sum_row -= prev_h * prev_cnt
                    cnt += prev_cnt
                stack.append((h, cnt))
                sum_row += h * cnt
                ans += sum_row

        return ans
        
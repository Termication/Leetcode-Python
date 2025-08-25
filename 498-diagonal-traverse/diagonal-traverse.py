class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m = len(mat)
        n = len(mat[0])
        result = []
        total_diagonals = m + n - 1
        
        for d in range(total_diagonals):
            if d % 2 == 0:
                i_min = max(0, d - n + 1)
                i_max = min(d, m - 1)
                for i in range(i_max, i_min - 1, -1):
                    j = d - i
                    result.append(mat[i][j])
            else:
                i_min = max(0, d - n + 1)
                i_max = min(d, m - 1)
                for i in range(i_min, i_max + 1):
                    j = d - i
                    result.append(mat[i][j])
                    
        return result
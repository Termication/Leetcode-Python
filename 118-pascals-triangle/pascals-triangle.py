class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for row_num in range(numRows):
            # Start each row with 1s, length = row_num + 1
            row = [1] * (row_num + 1)
            
            # Update internal values by summing the two numbers above
            for j in range(1, row_num):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            
            triangle.append(row)
        return triangle
            
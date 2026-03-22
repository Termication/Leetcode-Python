class Solution(object):
    @staticmethod
    def rotate(matrix):
        n = len(matrix)
        return [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]

    def findRotation(self, mat, target):
        for _ in range(4):  # check 0°, 90°, 180°, 270°
            if mat == target:
                return True
            mat = Solution.rotate(mat)  # call via class name
        return False

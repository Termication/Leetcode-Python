class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        max_diag_sq = 0
        max_area = 0
        for rect in dimensions:
            l, w = rect
            diag_sq = l * l + w * w
            area = l * w
            if diag_sq > max_diag_sq:
                max_diag_sq = diag_sq
                max_area = area
            elif diag_sq == max_diag_sq:
                if area > max_area:
                    max_area = area
        return max_area
        
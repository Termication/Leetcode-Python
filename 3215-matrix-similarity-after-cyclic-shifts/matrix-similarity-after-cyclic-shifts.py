class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        m, n = len(mat), len(mat[0])
        k = k % n  # effective shift

        for i in range(m):
            if k == 0:  # no shift needed
                continue
            if i % 2 == 0:  # even row → left shift
                shifted = mat[i][k:] + mat[i][:k]
            else:           # odd row → right shift
                shifted = mat[i][-k:] + mat[i][:-k]
            if shifted != mat[i]:
                return False
        return True

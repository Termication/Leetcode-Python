class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        sorted_indices = sorted(range(n), key=lambda i: -score[i])
        
        result = [""] * n
        for i, idx in enumerate(sorted_indices):
            if i == 0:
                result[idx] = "Gold Medal"
            elif i == 1:
                result[idx] = "Silver Medal"
            elif i == 2:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(i + 1)
        
        return result
        
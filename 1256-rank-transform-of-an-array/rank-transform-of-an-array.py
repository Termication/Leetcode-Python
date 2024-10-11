class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        '''Replaces each element in the array with its rank.'''
        # Create a sorted list of unique elements in the array
        sorted_unique = sorted(set(arr))

        # Create a dictionary that maps each element to its rank
        rank_map = {value: rank + 1 for rank, value in enumerate(sorted_unique)}

        # Replace each element in the original array with its rank
        return [rank_map[num] for num in arr]
        
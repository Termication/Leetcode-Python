class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """
        Checks if there exist two indices i and j such that:
        - i != j
        - 0 <= i, j < len(arr)
        - arr[i] == 2 * arr[j]
        
        Args:
            arr (list): List of integers.
            
        Returns:
            bool: True if such indices exist, False otherwise.
        """
        seen = set()
        for num in arr:
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False
    
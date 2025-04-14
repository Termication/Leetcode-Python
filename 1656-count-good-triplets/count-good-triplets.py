class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        """
        Counts the number of "good" triplets in an array based on given conditions.

        Args:
            arr: A list of integers.
            a: An integer representing the maximum absolute difference between arr[i] and arr[j].
            b: An integer representing the maximum absolute difference between arr[j] and arr[k].
            c: An integer representing the maximum absolute difference between arr[i] and arr[k].

        Returns:
            The number of good triplets in the array.
        """
        n = len(arr)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if abs(arr[i] - arr[j]) <= a and \
                    abs(arr[j] - arr[k]) <= b and \
                    abs(arr[i] - arr[k]) <= c:
                        count += 1
        return count
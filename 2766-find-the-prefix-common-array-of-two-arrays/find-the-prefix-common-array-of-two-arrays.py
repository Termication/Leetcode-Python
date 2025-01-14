class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """
        Calculates the prefix common array of two permutations A and B.

        Args:
            A: A 0-indexed integer permutation.
            B: A 0-indexed integer permutation.

        Returns:
            The prefix common array C.
        """
        n = len(A)
        C = [0] * n
        seen_in_a = set()
        seen_in_b = set()

        for i in range(n):
            seen_in_a.add(A[i])
            seen_in_b.add(B[i])
            common_count = 0
            for num in seen_in_a:
                if num in seen_in_b:
                    common_count += 1
            C[i] = common_count
        return C

    def find_prefix_common_array_optimized(A, B):
        """
        Calculates the prefix common array of two permutations A and B.
        Optimized version using a count array.

        Args:
            A: A 0-indexed integer permutation.
            B: A 0-indexed integer permutation.

        Returns:
            The prefix common array C.
        """

        n = len(A)
        C = [0] * n
        count = [0] * (n + 1) #Since the numbers are from 1 to n

        for i in range(n):
            if count[A[i]] == 1: #Already seen in B
                C[i] += 1
            else:
                count[A[i]] += 1
            
            if count[B[i]] == 1: #Already seen in A
                C[i] += 1
            else:
                count[B[i]] += 1

            if i > 0:
                C[i] += C[i-1] #Carry over the count from the prev index
        return C
            
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Step 1: Build the prefix XOR array
        n = len(arr)
        prefix = [0] * (n + 1)
        
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] ^ arr[i - 1]
        
        # Step 2: Answer each query using the prefix XOR array
        result = []
        for left, right in queries:
            result.append(prefix[right + 1] ^ prefix[left])
        
        return result
            
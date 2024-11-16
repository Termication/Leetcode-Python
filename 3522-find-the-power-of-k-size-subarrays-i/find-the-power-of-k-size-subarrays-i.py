class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        
        # Iterate over each subarray of size k
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            max_element = max(subarray)
            min_element = min(subarray)
            
            # Check if the subarray is sorted in ascending order
            is_sorted = True
            for j in range(1, k):
                if subarray[j] != subarray[j - 1] + 1:
                    is_sorted = False
                    break
            
            # Check if the subarray is consecutive and sorted
            if is_sorted and (max_element - min_element == k - 1):
                result.append(max_element)
            else:
                result.append(-1)
        
        return result
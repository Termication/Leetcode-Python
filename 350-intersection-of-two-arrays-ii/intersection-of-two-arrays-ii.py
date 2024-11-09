class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Step 1: Count the frequency of each element in both arrays
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        # Step 2: Find the intersection of the two counters
        intersection = count1 & count2
        
        # Step 3: Convert the intersection into a list with the correct frequency
        result = []
        for num, count in intersection.items():
            result.extend([num] * count)
        
        return result
            
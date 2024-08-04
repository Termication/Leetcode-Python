class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Initialize two pointers for each array
        i, j = 0, 0

        # Traverse both arrays until one of the pointers exceeds the length of its array
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                # If the current element in nums1 is smaller, move the pointer in nums1
                i += 1
            elif nums1[i] > nums2[j]:
                # If the current element in nums2 is smaller, move the pointer in nums2
                j += 1
            else:
                # If elements are equal, we found the minimum common value
                return nums1[i]
        
        # If no common element is found, return -1
        return -1
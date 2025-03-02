class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        """
        Merges two 2D arrays by summing values based on IDs.

        Args:
            nums1: The first 2D array.
            nums2: The second 2D array.

        Returns:
            The merged 2D array, sorted by ID.
        """
        merged_dict = {}

        for id, val in nums1:
            merged_dict[id] = merged_dict.get(id, 0) + val

        for id, val in nums2:
            merged_dict[id] = merged_dict.get(id, 0) + val

        result = sorted(merged_dict.items())
        return result
        
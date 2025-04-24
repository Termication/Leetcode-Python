class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_elements = set(nums)
        num_distinct = len(distinct_elements)
        n = len(nums)
        count = 0

        for i in range(n):
            subarray_elements = set()
            for j in range(i, n):
                subarray_elements.add(nums[j])
                if len(subarray_elements) == num_distinct:
                    count += (n - j)
                    break
                elif len(subarray_elements) > num_distinct:
                    break
        return count
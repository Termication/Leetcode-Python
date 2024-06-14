class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        write_index = 1  # Start writing from the second position

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # Only write unique elements
                nums[write_index] = nums[i]
                write_index += 1
        
        return write_index
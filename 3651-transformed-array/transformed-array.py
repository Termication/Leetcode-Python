class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        
        for i in range(n):
            if nums[i] == 0:
                result[i] = 0
            else:
                new_index = (i + nums[i]) % n
                result[i] = nums[new_index]
        
        return result

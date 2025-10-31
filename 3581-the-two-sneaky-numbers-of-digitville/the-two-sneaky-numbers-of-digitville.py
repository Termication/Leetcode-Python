class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) - 2
        count = {}
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        result = []
        for num, freq in count.items():
            if freq == 2:
                result.append(num)
        
        return result
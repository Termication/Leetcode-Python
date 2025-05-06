class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n  # Initialize the answer array with zeros
        
        for i in range(n):
            ans[i] = nums[nums[i]]
        
        return ans
            
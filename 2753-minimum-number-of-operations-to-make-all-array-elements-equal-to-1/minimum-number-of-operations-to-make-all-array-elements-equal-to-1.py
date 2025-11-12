class Solution(object):

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def minOperations(self, nums):
        n = len(nums)
    
        if 1 in nums:
            return sum(1 for x in nums if x != 1)
        
        total_gcd = nums[0]
        for num in nums[1:]:
            total_gcd = Solution.gcd(total_gcd, num)
        if total_gcd != 1:
            return -1
        
        min_len = float('inf')
        for i in range(n):
            curr_gcd = nums[i]
            for j in range(i + 1, n):
                curr_gcd = Solution.gcd(curr_gcd, nums[j])
                if curr_gcd == 1:
                    min_len = min(min_len, j - i + 1)
                    break
        
        return min_len - 1 + (n - 1)

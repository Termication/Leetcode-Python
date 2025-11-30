class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0
        
        seen = {0: -1}  # prefix remainder → index
        prefix = 0
        res = len(nums)
        
        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            # We want prefix - target ≡ some earlier prefix (mod p)
            need = (prefix - target) % p
            if need in seen:
                res = min(res, i - seen[need])
            seen[prefix] = i
        
        return res if res < len(nums) else -1
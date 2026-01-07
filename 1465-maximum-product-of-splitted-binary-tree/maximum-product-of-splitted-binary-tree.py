# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        MOD = 10**9 + 7
        self.subtree_sums = []
        
        # Step 1: compute total sum
        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            self.subtree_sums.append(s)
            return s
        
        total_sum = dfs(root)
        
        # Step 2: compute max product
        max_product = 0
        for s in self.subtree_sums:
            max_product = max(max_product, s * (total_sum - s))
        
        return max_product % MOD

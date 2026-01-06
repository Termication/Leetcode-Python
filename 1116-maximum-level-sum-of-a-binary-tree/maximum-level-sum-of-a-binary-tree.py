# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        queue = [root]   # use list instead of deque
        level = 1
        max_sum = float('-inf')
        answer = 1
        
        while queue:
            level_sum = 0
            next_level = []
            
            for node in queue:
                level_sum += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                answer = level
            
            queue = next_level
            level += 1
        
        return answer

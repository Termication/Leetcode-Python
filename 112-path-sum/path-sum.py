# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Checks if a binary tree has a root-to-leaf path with a given sum.

        Args:
            root: The root of the binary tree.
            targetSum: The target sum.

        Returns:
            True if a path exists, False otherwise.
        """
        if not root:
            return False

        def dfs(node, current_sum):
            if not node:
                return False

            current_sum += node.val

            if not node.left and not node.right:  # Leaf node
                return current_sum == targetSum

            return dfs(node.left, current_sum) or dfs(node.right, current_sum)

        return dfs(root, 0)
        
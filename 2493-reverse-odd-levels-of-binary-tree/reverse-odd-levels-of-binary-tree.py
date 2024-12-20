# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # BFS queue to traverse the tree level by level
        queue = [root]
        level = 0

        while queue:
            level_size = len(queue)
            current_level = []

            # Collect all nodes at the current level
            for _ in range(level_size):
                node = queue.pop(0)
                current_level.append(node)
                if node.left and node.right:
                    queue.append(node.left)
                    queue.append(node.right)

            # Reverse the values at odd levels
            if level % 2 == 1:
                values = [node.val for node in current_level]
                values.reverse()
                for i, node in enumerate(current_level):
                    node.val = values[i]

            level += 1

        return root

# Helper function to print tree in level-order for verification
def levelOrderTraversal(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
        
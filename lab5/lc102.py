from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_length = len(queue)
            current_level = []

            for _ in range(level_length):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result
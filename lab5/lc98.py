class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, left_bound, right_bound):
            if not node:
                return True

            if not (left_bound < node.val < right_bound):
                return False

            return (valid(node.left, left_bound, node.val) and
                    valid(node.right, node.val, right_bound))

        return valid(root, float('-inf'), float('inf'))
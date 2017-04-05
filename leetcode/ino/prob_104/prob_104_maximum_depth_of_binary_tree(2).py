# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def depth_stack(self, root):
        tree_stack = []
        max_depth = 0

        tree_stack.append((root, 1))

        while tree_stack.empty() is not True:
            cur_node, cur_depth = tree_stack.pop()

            if cur_node.left is not None:
                tree_stack.append((cur_node.left, cur_depth + 1))

            if cur_node.right is not None:
                tree_stack.append((cur_node.right, cur_depth + 1))

            max_depth = max(max_depth, cur_depth)

        return max_depth

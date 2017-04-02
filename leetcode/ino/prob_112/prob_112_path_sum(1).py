class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        node_stack = []
        sum_check = root.val

        node_stack.append((root,sum_check))

        while len(node_stack) > 0:
            node, sum_check = node_stack.pop()

            if node.left is None and node.right is None:  # then it is leaf
                if sum_check == sum:
                    return True

            if node.left is not None and node.right is not None:
                node_stack.append((node.left, sum_check + node.left.val))
                node_stack.append((node.right, sum_check + node.right.val))
            if node.left is not None and node.right is None:
                node_stack.append((node.left, sum_check + node.left.val))
            if node.left is None and node.right is not None:
                node_stack.append((node.right, sum_check + node.right.val))

        return False
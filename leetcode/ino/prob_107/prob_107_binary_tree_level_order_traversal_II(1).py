class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return []

        node_queue = []
        level_stack = []
        level_arr = []
        result = []
        cur_level = 1

        # push node into queue, as (node, level)
        node_queue.append((root,cur_level))

        while len(node_queue) > 0:
            node, node_level = node_queue.pop(0)

            if node_level > cur_level:
                cur_level = node_level
                level_stack.append(level_arr)
                level_arr = []

            level_arr.append(node.val)

            if node.left is not None and node.right is not None:
                node_queue.append((node.left, node_level + 1))
                node_queue.append((node.right, node_level + 1))
            elif node.left is not None and node.right is None:
                node_queue.append((node.left, node_level + 1))
            elif node.left is None and node.right is not None:
                node_queue.append((node.right, node_level + 1))

        if len(level_arr) > 0:
            level_stack.append(level_arr)

        while len(level_stack) > 0:
            result.append(level_stack.pop())

        return result

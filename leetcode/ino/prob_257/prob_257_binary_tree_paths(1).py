# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def path_by_dfs(self, node, result, path):
        if node is None:
            return

        if node.left is None and node.right is None:
            result.append(path + str(node.val))
            return

        path = path + str(node.val) + '->'

        self.path_by_dfs(node.left, result, path)
        self.path_by_dfs(node.right, result, path)


    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        result = []
        path = ""
        self.path_by_dfs(root, result, path)

        return result


test_arr = []
root = None
cur = None
queue = []
for i in range(0, len(test_arr), 2):
    if i == 0:
        root = TreeNode(test_arr[i])
        queue.append(root)
    else:
        cur = queue.pop(0)
        cur.left = TreeNode(test_arr[i-1])
        cur.right = TreeNode(test_arr[i])
        queue.append(cur.left)
        queue.append(cur.right)

obj = Solution()
result = obj.binaryTreePaths(root)
print(result)
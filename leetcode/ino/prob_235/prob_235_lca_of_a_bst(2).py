# iterative solution
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return None

        a = 0
        b = 0
        cur = root
        if p.val <= q.val:
            a, b = p.val, q.val
        else:
            a, b = q.val, p.val

        while not (a <= cur.val <= b):
            if cur is None:
                break

            if b < cur.val:
                cur = cur.left
            elif cur.val < a:
                cur = cur.right

        return cur


test_arr = [6,2,8,0,4,7,9]
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


p = TreeNode(2)
q = TreeNode(4)

obj = Solution()
result = obj.lowestCommonAncestor(root, p, q)
if result is None:
    print(result)
else:
    print(result.val)

class Solution(object):

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        result = ''

        pass_dir = ['', '.']
        stack = []

        for dir in path:
            if dir not in pass_dir:
                if dir == '..':
                    if len(stack) > 0:
                        stack.pop()
                else:
                    stack.append(dir)
            else:
                continue

        while len(stack) > 0:
            adder = stack.pop()
            result = '/' + adder + result
        if result == '':
            return '/'
        return result


obj = Solution()
path = "/home/..."
print(obj.simplifyPath(path))

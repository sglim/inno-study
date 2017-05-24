class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')


x = 1
y = 4
obj = Solution()
print(obj.hammingDistance(x, y))

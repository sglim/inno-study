class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 0:
            return False

        while n & 1 != 1:
            n = n >> 1

        if n == 1:
            return True
        else:
            return False


obj = Solution()
n = 2**1 + 4

print(obj.isPowerOfTwo(n))

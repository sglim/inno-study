# time limit...

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
        if x == 0:
            return 0

        i = 1
        while i*i <= x:
            i += 1

        return i - 1

obj = Solution()
x = 15
print(obj.mySqrt(x))



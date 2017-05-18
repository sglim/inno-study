'''
*Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
'''
import math

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        epsilon = 0.0000001

        return (math.log(num) / math.log(2)) % 2 <= epsilon

obj = Solution()
num = 2**29
print(obj.isPowerOfFour(num))

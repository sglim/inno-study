'''
using epsilon due to precision error.
ex) math.log2(2^5) / math.log2(2) = 5.000001 or 4.999999...
be careful when select value of epsilon.
'''

import math

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        epsilon = 0.00000000001
        return (math.log10(n) / math.log10(3)) % 1 + epsilon <= 2*epsilon


obj = Solution()
n = 129140164
print(obj.isPowerOfThree(n))

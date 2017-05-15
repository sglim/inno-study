# fail : time limit

import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return 0

        count = 0
        for num in range(2, n):
            limit = int(math.sqrt(num))
            prime = True
            for i in range(2, limit+1):
                if num % i == 0:
                    prime = False

            if prime:
                count += 1

        return count



obj = Solution()
n = 1500000
print(obj.countPrimes(n))

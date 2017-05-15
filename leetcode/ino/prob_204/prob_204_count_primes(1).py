# fail : memory limit

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return 0

        checker = [1] * n
        checker[0] = 0
        checker[1] = 0

        for i in range(2, int(n**0.5) + 1):
            if checker[i]:
                checker[2*i:n:i] = [0] * len(checker[2*i:n:i])

        return sum(checker)


obj = Solution()
n = 3
print(obj.countPrimes(n))

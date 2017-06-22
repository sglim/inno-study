'''

let d[n] : number of ways to climbing n-stairs
then :
    d[n] = d[n-1] + d[n-2]

'''


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0

        d = {0: 0, 1: 1, 2: 2}
        if n <= 2:
            return d[n]

        for i in range(3, n + 1):
            d[i] = d[i-1] + d[i-2]

        return d[n]


obj = Solution()
n = 3

print(obj.climbStairs(n))

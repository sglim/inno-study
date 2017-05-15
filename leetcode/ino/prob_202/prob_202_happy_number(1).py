class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dummy = n

        while n != 1:
            temp = 0
            while n != 0:
                temp += (n % 10) ** 2
                n //= 10
            n = temp
            if n == dummy:
                return False

        return True


obj = Solution()
n = 132
print(obj.isHappy(n))

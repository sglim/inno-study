class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max = 2**31 - 1
        min = -2**31
        flag = False

        if x < 0:
            x *= -1
            flag = True

        result = 0
        while x:
            digit = x % 10
            result = result * 10 + digit
            x //= 10

        if flag:
            result *= -1

        if result < min or max < result:
            return 0

        return result


test = 123
obj = Solution()
print(obj.reverse(test))

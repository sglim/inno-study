class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        if num == 1:
            return True

        sq = 1
        adder = 3

        while sq < num:
            sq += adder
            adder += 2

        if sq == num:
            return True
        else:
            return False


num = 2147483647
obj = Solution()
print(obj.isPerfectSquare(num))

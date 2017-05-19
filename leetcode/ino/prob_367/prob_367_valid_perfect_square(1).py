'''
time limit fail
'''

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

        div = 2
        while num > 1 and div <= num:
            count = 0
            while num % div == 0:
                num /= div
                count += 1

            if count % 2 == 1:
                return False

            div += 1

        return True


num = 2147483647
obj = Solution()
print(obj.isPerfectSquare(num))

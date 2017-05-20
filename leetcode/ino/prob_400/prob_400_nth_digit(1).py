# time limit fail

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        i = 1
        while count < n:
            num = i
            while num > 0:
                num //= 10
                count += 1
            i += 1

        #number that includes nth digit
        last_num = i - 1

        # count back amount of : count - n
        result = last_num % 10
        back = count - n
        while back > 0:
            last_num //= 10
            result = last_num % 10
            back -= 1
        return result


n = 100000000
obj = Solution()
print(obj.findNthDigit(n))

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n

        order_idx = 1
        temp = n
        k = 0
        while temp > 0:
            k = temp
            temp -= order_idx * 9 * 10**(order_idx - 1)
            order_idx += 1
        order_idx -= 1

        # now nth digit is located kth position of order_idx's range
        n_include_num = 10**(order_idx - 1) + (k//order_idx) - 1
        if k % order_idx != 0:
            n_include_num += 1

        #target digit is located 'order_idx + 1 - k%order_idx'th from back of n_include_num
        back = 0
        if k % order_idx == 0:
            back = 1
        else:
            back = (order_idx + 1) - (k % order_idx)

        result = 0
        for i in range(back):
            result = n_include_num % 10
            n_include_num //= 10

        return result



n = 2147483647
# n = 17
obj = Solution()
print(obj.findNthDigit(n))

# print(2**31-1)

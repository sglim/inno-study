# should study bit manipulation !!

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        max_int = 2**31 - 2
        mask = 0b11111111111111111111111111111111
        while b != 0:
            bit_sum = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = bit_sum
            b = carry

        if a <= max_int:
            return a
        else:
            return ~(a ^ mask)


a = -12
b = -8

obj = Solution()
print(obj.getSum(a, b))

#
# class Solution(object):
#     def getSum(self, a, b):
#         """
#         :type a: int
#         :type b: int
#         :rtype: int
#         """
#         # 32 bits integer max
#         MAX = 0x7FFFFFFF
#         # 32 bits interger min
#         MIN = 0x80000000
#         # mask to get last 32 bits
#         mask = 0xFFFFFFFF
#         while b != 0:
#             # ^ get different bits and & gets double 1s, << moves carry
#             a, b = (a ^ b) & mask, ((a & b) << 1) & mask
#         # if a is negative, get a's 32 bits complement positive first
#         # then get 32-bit positive's Python complement negative
#         return a if a <= MAX else ~(a ^ mask)

# print(int('0x7FFFFFFF',16))
# print(2**31 - 1)
#
# print(int('0x80000000', 16))
# print(2**31)
#
# print(bin(int('0xFFFFFFFF',16)))
#
# a = 5
# print(bin(a))
# print(bin(~a))
# print(bin(a + ~a))
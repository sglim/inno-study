'''
in python, max_int = sys.maxsize = 9,223,372,036,854,775,807
we can find that
    
    3^40 = 12,157,665,459,056,928,801 > 9,223,372,036,854,775,807 = max_int
    3^39 = 4,052,555,153,018,976,267 < 9,223,372,036,854,775,807 = max_int
    
thus 3^39 is largest power of 3 in practical number range.
so for any given n, that should be divisible 3^39 if that is power of 3 in our number range.
'''


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        return 4052555153018976267 % n == 0


obj = Solution()
n = 129140164
print(obj.isPowerOfThree(n))

# max_int = sys.maxsize
# print(max_int)
#
# i = 10
# n = 3 ** i
# while n <= max_int:
#     n *= 3
#     i += 1
#
# print(n, i)
# print(3**(i-1))

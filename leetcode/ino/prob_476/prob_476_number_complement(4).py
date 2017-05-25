class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = ~0
        while mask & num:
            mask = mask << 1

        return ~mask & ~num


num = 5
obj = Solution()
print(obj.findComplement(num))

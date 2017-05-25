class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        dummy = num
        order = 1
        while dummy > 0:
            dummy = dummy >> 1
            order = order << 1
            order |= 1

        return (order >> 1) ^ num

num = 5
obj = Solution()
print(obj.findComplement(num))

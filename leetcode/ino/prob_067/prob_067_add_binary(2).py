class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a = int(a,2)
        b = int(b,2)

        return str(bin(a+b))[2:]


sol = Solution()
a = '1011'
b = '1'

print(sol.addBinary(a,b))
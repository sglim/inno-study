class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        temp = 0
        offset = ord('0')
        result = ''

        a_idx = len(a) - 1
        b_idx = len(b) - 1

        while a_idx >= 0 or b_idx >= 0 or temp != 0:
            if a_idx >= 0:
                temp += (ord(a[a_idx]) - offset)
                a_idx -= 1
            if b_idx >= 0:
                temp += (ord(b[b_idx]) - offset)
                b_idx -= 1

            result = chr(int(temp % 2) + offset) + result
            temp //= 2

        return result


sol = Solution()
a = ''
b = ''

print(sol.addBinary(a,b))
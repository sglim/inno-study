class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        if len(a) >= len(b):
            longer = a
            shorter = b
        else:
            longer = b
            shorter = a

        result = ''
        idx = len(longer) - 1
        upper_digit = 0

        for digit in shorter[::-1]:
            if digit == '0' and longer[idx] == '0':
                if upper_digit == 1:
                    result = '1' + result
                    upper_digit = 0
                else:
                    result = '0' + result
                idx -= 1
            elif digit == '1' and longer[idx] == '1':
                if upper_digit == 1:
                    result = '1' + result
                else:
                    result = '0' + result
                    upper_digit = 1
                idx -= 1
            else:
                if upper_digit == 1:
                    result = '0' + result
                else:
                    result = '1' + result
                idx -= 1

        for i in range(idx,-1,-1):
            if upper_digit == 1:
                if longer[i] == '0':
                    result = '1' + result
                    upper_digit = 0
                else:
                    result = '0' + result
                    upper_digit = 1
            else:
                if longer[i] == '0':
                    result = '0' + result
                else:
                    result = '1' + result

        if upper_digit == 1:
            result = '1' + result

        return result



sol = Solution()
a = '11'
b = '1'

print(sol.addBinary(a,b))
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        num_map = {'I': 1,
                   'V': 5,
                   'X': 10,
                   'L': 50,
                   'C': 100,
                   'D': 500,
                   'M': 1000}

        result = 0
        i = 0
        length = len(s)
        while i < length:
            num = num_map[s[i]]
            if i < length - 1 and num < num_map[s[i+1]]:
                result = result + num_map[s[i+1]] - num
                i += 2
            else:
                result += num
                i += 1

        return result


obj = Solution()
print(obj.romanToInt('XCIV'))

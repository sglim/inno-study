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
        for i in range(len(s)-1):
            num = num_map[s[i]]
            next_num = num_map[s[i+1]]
            if num < next_num:
                num *= -1

            result += num

        result += num_map[s[-1]]

        return result


obj = Solution()
print(obj.romanToInt('XCIV'))

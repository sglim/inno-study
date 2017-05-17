class Solution(object):
    def pattern_checker(self, arr):
        check_hash = {}
        cur = 0
        result = []
        for ch in arr:
            if ch in check_hash:
                result.append(check_hash[ch])
            else:
                cur += 1
                check_hash[ch] = cur
                result.append(cur)
        return result

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern_arr = []
        for char in pattern:
            pattern_arr.append(char)

        str_arr = str.split()

        return self.pattern_checker(pattern_arr) == self.pattern_checker(str_arr)


pattern = 'abab'
str_input = 'dog cat cat dog'

obj = Solution()
print(obj.wordPattern(pattern, str_input))

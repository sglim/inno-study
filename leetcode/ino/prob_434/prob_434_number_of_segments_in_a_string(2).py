class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag = False
        count = 0
        for i in range(len(s)):
            if s[i] == ' ':
                flag = False
            elif s[i] != ' ' and flag is False:
                flag = True
                count += 1

        return count


input_str = " hi   hello"
obj = Solution()
print(obj.countSegments(input_str))

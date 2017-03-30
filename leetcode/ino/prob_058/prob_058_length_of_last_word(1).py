class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        s = s.strip(' ')

        if s == '':
            return count

        for ch in s[::-1]:
            if ch == ' ':
                break
            else:
                count += 1

        return  count



sol = Solution()
test_str = "a "

print(sol.lengthOfLastWord(test_str))

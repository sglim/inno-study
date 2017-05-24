class Solution(object):
    def can_check(self, candidate, can_len, s):
        for j in range(0, len(s), can_len):
            if candidate != s[j:j+can_len]:
                return False
        return True


    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        total_len = len(s)
        end = s[total_len - 1]
        flag = False

        for i in range(0, total_len):
            if s[i] == end:
                candidate = s[0:i + 1]
                can_len = len(candidate)

                if can_len > (total_len // 2):
                    break

                if total_len % can_len != 0:
                    continue

                if self.can_check(candidate, can_len, s[i+1:]):
                    flag = True
                    break

        return flag

s = 'a'
obj = Solution()
print(obj.repeatedSubstringPattern(s))
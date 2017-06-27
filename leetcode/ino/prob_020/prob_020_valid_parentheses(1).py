class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        open_ch = '([{'

        for char in s:
            if char in open_ch:
                stack.append(char)
            else:
                opp_ch = ''
                if len(stack):
                    opp_ch = stack.pop()

                if char == ')' and opp_ch != '(':
                    return False
                elif char == ']' and opp_ch != '[':
                    return False
                elif char == '}' and opp_ch != '{':
                    return False

        if len(stack):
            return False

        return True


obj = Solution()
input_str = '((([]))'
print(obj.isValid(input_str))

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        original = x
        checker = 0

        while checker < x:
            checker *= 10
            checker += original%10
            original //= 10

        return x == checker

sol = Solution()

test_input = 100

print(sol.isPalindrome(test_input))
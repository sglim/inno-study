class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        last = int(len(x)/2)
        for i in range(last):
            if x[i] != x[len(x)-i-1]:
                return False

        return True


sol = Solution()

test_input = 128799821

print(sol.isPalindrome(test_input))
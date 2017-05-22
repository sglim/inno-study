class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odd_flag = False
        length = 0
        frequency = [0] * 52

        for char in s:
            if ord(char) >= ord('a'):
                idx = ord(char) - ord('a') + 26
            else:
                idx = ord(char) - ord('A')

            frequency[idx] += 1

        for freq in frequency:
            if freq == 0:
                continue
            elif freq % 2 == 0:
                length += freq
            else:
                if odd_flag:
                    length += (freq - 1)
                else:
                    length += freq
                    odd_flag = True

        if length > 1010:
            length = 1010

        return length


in_str = "abccccdd"
obj = Solution()
print(obj.longestPalindrome(in_str))

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        if len(ransomNote) == 0:
            return True

        if len(magazine) == 0 or len(magazine) < len(ransomNote):
            return False

        memo_list = [0] * 26  # assume input strings consist of lowercase letters only and ascii code
        for char in ransomNote:
            idx = ord(char) - ord('a')
            memo_list[idx] += 1

        for char in magazine:
            idx = ord(char) - ord('a')
            if memo_list[idx] == 0:
                continue
            else:
                memo_list[idx] -= 1

        return sum(memo_list) == 0


ransom = 'aa'
magazine = 'ab'

obj = Solution()
print(obj.canConstruct(ransom, magazine))

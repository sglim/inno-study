'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
'''


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = 'aeiouAEIOU'

        left = 0
        right = len(s) - 1
        s = list(s)

        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1

        return ''.join(s)



test_str = "A man a plan"
obj = Solution()
print(obj.reverseVowels(test_str))



# def reverseVowels(self, s):
#     vowels = re.findall('(?i)[aeiou]', s)
#     return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)


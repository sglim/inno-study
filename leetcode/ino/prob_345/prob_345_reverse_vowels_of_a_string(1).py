# fail. time limit

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
    def get_left_vowels(self, s, left, vowels):
        last_idx = len(s) - 1
        while left <= last_idx:
            left += 1
            if left > last_idx or s[left] in vowels:
                break

        return left

    def get_right_vowels(self, s, right, vowels):
        while 0 <= right:
            right -= 1
            if right < 0 or s[right] in vowels:
                break

        return right

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''

        vowels = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True,
                  'A': True, 'E': True, 'I': True, 'O': True, 'U': True}

        input_str = []
        for ch in s:
            input_str.append(ch)

        left = 0
        if not input_str[left] in vowels:
            left = self.get_left_vowels(input_str, left, vowels)

        right = len(input_str) - 1
        if not input_str[right] in vowels:
            right = self.get_right_vowels(input_str, right, vowels)

        while left < right:
            input_str[left], input_str[right] = input_str[right], input_str[left]
            left = self.get_left_vowels(input_str, left, vowels)
            right = self.get_right_vowels(input_str, right, vowels)

        result = ''
        for ch in input_str:
            result += ch

        return result


test_str = "A a"
obj = Solution()
print(obj.reverseVowels(test_str))

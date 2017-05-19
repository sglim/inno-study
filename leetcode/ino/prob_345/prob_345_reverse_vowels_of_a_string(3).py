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
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True,
                  'A': True, 'E': True, 'I': True, 'O': True, 'U': True}

        input_str = []
        for ch in s:
            input_str.append(ch)

        stack = []

        for i in range(len(input_str)):
            if input_str[i] in vowels:
                stack.append(input_str[i])

        for i in range(len(input_str)):
            if input_str[i] in vowels:
                input_str[i] = stack.pop()

        result = ''
        for ch in input_str:
            result += ch

        return result

test_str = "A man a plan"
obj = Solution()
print(obj.reverseVowels(test_str))



# def reverseVowels(self, s):
#     vowels = re.findall('(?i)[aeiou]', s)
#     return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)


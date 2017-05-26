class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        first = {'q': 0, 'w': 0, 'e': 0, 'r': 0, 't': 0, 'y': 0, 'u': 0, 'i': 0, 'o': 0, 'p': 0,
                 'Q': 0, 'W': 0, 'E': 0, 'R': 0, 'T': 0, 'Y': 0, 'U': 0, 'I': 0, 'O': 0, 'P': 0}
        second = {'a': 0, 's': 0, 'd': 0, 'f': 0, 'g': 0, 'h': 0, 'j': 0, 'k': 0, 'l': 0,
                  'A': 0, 'S': 0, 'D': 0, 'F': 0, 'G': 0, 'H': 0, 'J': 0, 'K': 0, 'L': 0}
        third = {'z': 0, 'x': 0, 'c': 0, 'v': 0, 'b': 0, 'n': 0, 'm': 0,
                 'Z': 0, 'X': 0, 'C': 0, 'V': 0, 'B': 0, 'N': 0, 'M': 0}
        hash_set = [first, second, third]

        result = []
        for word in words:
            row = 0
            flag = True
            if word[0] in second:
                row = 1
            elif word[0] in third:
                row = 2

            for char in word[1:]:
                if char not in hash_set[row]:
                    flag = False
                    break
            if flag:
                result.append(word)
        return result


words = ["Hello", "Alaska", "Dad", "Peace"]
obj = Solution()
print(obj.findWords(words))

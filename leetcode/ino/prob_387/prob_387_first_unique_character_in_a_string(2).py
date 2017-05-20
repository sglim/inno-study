'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''


# 82.25% runtime distribution

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        #  1. 순서대로 탐방하면서, 해당 문자를 candidate로 둔다.
        #  2. candidate가 기존에 이미 지나온 문자이면 탈락. 탈락 후보군으로 이동한다.
        #  3. 탈락군으로 이동하지 않고 답후보에 마지막까지 남아있는 문자가 정답.

        ans_candidates = {}
        checker_hash = {}

        for i in range(len(s)):
            #  char에 대한 경우의 수:
            #  1. 이미 마주친 문자이다:
            #       -1. ans에 현재 후보군으로 등록되어 있었거나
            #           -ans 정보를 삭제하고(후보없음) 해당 문자를 탈락군으로 이동시킨다.
            #       -2. 이미 탈락군으로 이동했다
            #           - pass.
            #
            #  2. 마주친적이 없다:
            #       -문자, 인덱스 정보를 'ans'에 저장.
            char = s[i]

            if char in checker_hash:
                continue
            elif char in ans_candidates:
                checker_hash[char] = 1
            else:
                ans_candidates[char] = i

        result = 2147483647  # 2**31 - 1
        flag = False
        for char in ans_candidates:
            if char not in checker_hash:
                flag = True
                result = min(result, ans_candidates[char])

        if flag:
            return result
        else:
            return -1


input_str = 'loveleetcode'
obj = Solution()
print(obj.firstUniqChar(input_str))

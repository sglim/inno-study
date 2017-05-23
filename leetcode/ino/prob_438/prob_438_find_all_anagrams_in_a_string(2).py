class Solution(object):
    def char_to_idx(self, c):
        return ord(c) - ord('a')

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        len_s = len(s)
        len_p = len(p)
        if len_s < len_p:
            return []

        result = []
        s_hash = [0] * 26
        p_hash = [0] * 26

        for c in p:
            p_hash[self.char_to_idx(c)] += 1

        for c in s[:len_p-1]:
            s_hash[self.char_to_idx(c)] += 1

        for i in range(len_s - len_p + 1):
            add_idx = i + len_p - 1
            del_idx = i - 1

            idx = self.char_to_idx(s[add_idx])
            s_hash[idx] += 1

            if del_idx >= 0:
                idx = self.char_to_idx(s[del_idx])
                s_hash[idx] -= 1

            if s_hash == p_hash:
                result.append(i)

        return result


s = "abab"
p = "ab"
obj = Solution()
print(obj.findAnagrams(s, p))

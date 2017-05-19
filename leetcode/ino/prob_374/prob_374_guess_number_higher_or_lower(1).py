# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
ans = 10


def guess(num):
    if num == ans:
        return 0
    elif num < ans:
        return 1
    else:
        return -1


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lower = 1
        higher = n
        result = 0
        while lower <= higher:
            mid = (lower + higher) // 2
            if guess(mid) < 0:
                higher = mid - 1
            elif guess(mid) > 0:
                lower = mid + 1
            else:
                result = mid
                break

        return result


n = 10
obj = Solution()
print(obj.guessNumber(n))

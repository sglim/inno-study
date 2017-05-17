# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
bad = 5
def isBadVersion(version):
    return bad <= version

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n

        while start < end:
            mid = start + (end - start) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1

        return start


obj = Solution()
print(obj.firstBadVersion(100))
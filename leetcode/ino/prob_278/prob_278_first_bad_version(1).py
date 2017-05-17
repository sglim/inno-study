# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
bad = 0
def isBadVersion(version):
    return bad <= version

class Solution(object):
    def get_mid(self, start, end):
        return (start + end)//2

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n + 1
        mid = self.get_mid(start, end)

        while True:
            if isBadVersion(mid):
                if mid == 1:
                    return mid
                if not isBadVersion(mid-1):
                    return mid
                end = mid
                mid = self.get_mid(start, end)
            else:
                if mid == n:
                    return None
                start = mid
                mid = self.get_mid(start, end)


obj = Solution()
print(obj.firstBadVersion(100))
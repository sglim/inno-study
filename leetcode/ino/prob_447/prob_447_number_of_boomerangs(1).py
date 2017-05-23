class Solution(object):
    def dist(self, a, b):
        x1, y1 = a[0], a[1]
        x2, y2 = b[0], b[1]
        return (x1 - x2)**2 + (y1 - y2)**2

    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0

        for a in points:
            checker = {}
            for b in points:
                if a == b:
                    continue

                dis = self.dist(a, b)
                checker.setdefault(dis, 0)
                checker[dis] += 1

            for dis in checker:
                result += checker[dis] * (checker[dis] - 1)

        return result


points = [[0,0],[1,0],[2,0]]
obj = Solution()
print(obj.numberOfBoomerangs(points))


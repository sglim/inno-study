class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex < 0:
            return []
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]

        result_row = [1,1]
        for i in range(rowIndex - 1):
            result_row = result_row + [1]
            for j in range(len(result_row)-2, 0, -1):
                result_row[j] = result_row[j] + result_row[j-1]

        return result_row

sol = Solution()
print(sol.getRow(5))
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex < 0:
            return []

        result_row = [1]
        if rowIndex == 0:
            return result_row

        for i in range(rowIndex):
            augmented_row = result_row + [0]
            for j in range(len(result_row)):
                augmented_row[j+1] = augmented_row[j+1] + result_row[j]

            result_row = augmented_row

        return result_row

sol = Solution()
print(sol.getRow(3))
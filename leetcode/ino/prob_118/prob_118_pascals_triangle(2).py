class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows <= 0:
            return []

        triangle_result = [[1]]

        if numRows == 1:
            return triangle_result

        for i in range(1,numRows):
            before_row = triangle_result[len(triangle_result) - 1]
            augmented_row = before_row + [0]

            for i in range(len(before_row)):
                augmented_row[i+1] = augmented_row[i+1] + before_row[i]

            triangle_result.append(augmented_row)

        return triangle_result

sol = Solution()
print (sol.generate(5))
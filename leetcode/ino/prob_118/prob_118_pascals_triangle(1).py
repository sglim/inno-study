class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows <= 0:
            return []

        if numRows == 1:
            return [[1]]

        if numRows >= 2:
            triangle_result = self.generate(numRows - 1)
            last_row = triangle_result[len(triangle_result) - 1]
            new_row = self.calculate_row(last_row)
            triangle_result.append(new_row)
            return triangle_result

    def calculate_row(self, last_row):
        augmented_row = last_row + [0]
        result = [1]
        for i in range(len(last_row)):
            temp = augmented_row[i+1] + last_row[i]
            result.append(temp)
        return result

sol = Solution()
print (sol.generate(3))
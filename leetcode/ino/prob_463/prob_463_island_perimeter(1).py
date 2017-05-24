class Solution(object):
    def check_neighbor(self, grid, i, j, row_len, col_len):
        count = 0
        if grid[i][j]:
            di = [1, -1, 0, 0]
            dj = [0, 0, 1, -1]

            for k in range(4):
                ii = i + di[k]
                jj = j + dj[k]

                if 0 <= ii < row_len and 0 <= jj < col_len:
                    if grid[ii][jj]:
                        count += 1
        return count

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lands = 0
        count = 0
        row_len = len(grid)
        col_len = len(grid[0])

        for i in range(row_len):
            for j in range(col_len):
                lands += grid[i][j]
                count += self.check_neighbor(grid, i, j, row_len, col_len)

        return 4 * lands - count


input_grid = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
obj = Solution()
print(obj.islandPerimeter(input_grid))

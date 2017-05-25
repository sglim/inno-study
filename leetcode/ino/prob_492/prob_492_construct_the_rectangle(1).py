class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        start = int(area ** 0.5)
        result = [0, 0]

        # to avoid memory exceeding, for loop should be proceed into small number
        for i in range(start, 0, -1):
            if area % i == 0:
                result[1] = i
                result[0] = area // i
                break

        return result


input_area = 10000000
obj = Solution()
print(obj.constructRectangle(input_area))

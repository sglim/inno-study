class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        min_val = -2 ** 31 - 1

        result = [min_val, min_val, min_val]  # assume this is pre-sorted (by maximum) list. this list will keep its sorted order
        checker = {}

        for num in nums:
            if num in checker:
                continue
            else:
                checker[num] = True
                if num > result[0]:
                    result[0], result[1], result[2] = num, result[0], result[1]

                elif num > result[1] and num != result[0]:
                    result[1], result[2] = num, result[1]

                elif num > result[2] and num != result[0] and num != result[1]:
                    result[2] = num

        if result[2] == min_val:
            return result[0]

        else:
            return result[2]


nums = [1,2,2,5,3,5]
obj = Solution()
print(obj.thirdMax(nums))


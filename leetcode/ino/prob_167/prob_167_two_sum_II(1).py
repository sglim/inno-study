class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        check_hash = {}

        length = len(numbers)
        for i in range(1, length):
            if numbers[i] in check_hash:
                idx = check_hash[numbers[i]]

                return [idx, i]
            else:
                check_hash[target - numbers[i]] = i

        return None


obj = Solution()

numbers = [0, 2, 3, 4]
target = 6

print(obj.twoSum(numbers, target))

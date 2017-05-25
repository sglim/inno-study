class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_consec = 0
        count = 0
        for num in nums:
            if num == 0:
                max_consec = max(max_consec, count)
                count = 0
            else:
                count += 1

        return max(max_consec, count)

input_arr = [1,1,0,1,1,1]
obj = Solution()
print(obj.findMaxConsecutiveOnes(input_arr))

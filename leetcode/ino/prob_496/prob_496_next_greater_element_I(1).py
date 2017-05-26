# naive approach : ~O(n^2)

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for num1 in findNums:
            flag = False
            find = False
            for num2 in nums:
                if num2 == num1:
                    flag = True
                elif flag and num2 > num1:
                    result.append(num2)
                    find = True
                    break
            if not find:
                result.append(-1)

        return result


nums1 = [4,1,2]
nums2 = [1,3,4,2]

obj = Solution()
print(obj.nextGreaterElement(nums1, nums2))


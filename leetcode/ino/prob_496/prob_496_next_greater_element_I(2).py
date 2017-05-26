# using hash and stack.

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        if len(findNums) == 0:
            return result
        greater_hash = {}
        stack = []
        stack.append(nums[0])
        greater_hash[nums[0]] = -1
        for num2 in nums[1:]:
            greater_hash[num2] = -1
            if num2 < stack[-1]:
                stack.append(num2)
            else:
                while len(stack) != 0 and num2 > stack[-1]:
                    small = stack.pop()
                    greater_hash[small] = num2
                stack.append(num2)

        for num1 in findNums:
            result.append(greater_hash[num1])

        return result


nums1 = [1,3,5,2,4]
nums2 = [5,4,3,2,1]

obj = Solution()
print(obj.nextGreaterElement(nums1, nums2))


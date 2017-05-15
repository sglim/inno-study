class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        major_length = n//2

        check_hash = {}
        max_count_pair = [0, 0]  # num, count

        for num in nums:
            if num in check_hash:
                check_hash[num] += 1
            else:
                check_hash[num] = 1

        for key in check_hash:
            if check_hash[key] > max_count_pair[1]:
                max_count_pair[0] = key
                max_count_pair[1] = check_hash[key]

        return max_count_pair[0]


obj = Solution()

test_arr = [1,2]
print(obj.majorityElement(test_arr))

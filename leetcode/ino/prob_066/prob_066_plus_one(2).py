class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        last_idx = len(digits) - 1

        digits[last_idx] += 1

        if digits[last_idx] >= 10:
            for i in range(last_idx,0,-1):
                if digits[i] >= 10:
                    digits[i-1] += 1
                    digits[i] = 0

            if digits[0] >= 10:
                new_digits = [1]
                digits[0] = 0

                for num in digits:
                    new_digits.append(num)

                digits = new_digits

        return digits


sol = Solution()
test = [9,9]

print(sol.plusOne(test))
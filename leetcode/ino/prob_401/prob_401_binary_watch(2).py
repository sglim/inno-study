'''
solution by StefanPochmann
'''

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        result = []

        for hour in range(12):
            for minute in range(60):
                if (bin(hour) + bin(minute)).count('1') == num:
                    result.append('%d:%02d' % (hour, minute))

        return result


num = 4
obj = Solution()
result = obj.readBinaryWatch(num)
result.sort()
print(result)

# test = ['%d--%02d' % (a, b) for a in range(2) for b in range(3)]
# print(test)
# str_test = 'abcdde'



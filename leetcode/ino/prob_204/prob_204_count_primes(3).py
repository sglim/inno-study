# fail : time limit

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return 0

        count = 1
        dividers = [2]
        for num in range(3, n):
            prime = True

            for div in dividers:
                if num % div == 0:
                    prime = False

            if prime:
                count += 1
                dividers.append(num)

        return count


obj = Solution()
n = 1000
print(obj.countPrimes(n))

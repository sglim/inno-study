class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0

        for i in range(32):
            result = result * 2 + (n % 2)
            n //= 2

        return result


obj = Solution()
n = 43261596
print(obj.reverseBits(n))

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        fizz = 0
        buzz = 0

        for i in range(1, n + 1):
            fizz += 1
            buzz += 1
            if fizz == 3 and buzz == 5:
                result.append('FizzBuzz')
                fizz = 0
                buzz = 0

            elif fizz == 3:
                result.append('Fizz')
                fizz = 0

            elif buzz == 5:
                result.append('Buzz')
                buzz = 0

            else:
                result.append(str(i))

        return result


n = 15
obj = Solution()
print(obj.fizzBuzz(n))

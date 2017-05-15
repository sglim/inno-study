'''
if we execute 'square-sum cycle' repeatedly for arbitrary large number n >= 100,
eventually the number will be shrunk into < 100 (two(2) order number).
here is why :

let n is some arbitrary, large, larger number, say 9999999....9, and its order is k (9 repeated kth)
if we execute 'square-sum cycle' once, the result is:

    9999999....9 -> 9^2 * k

let's check this in detail:
    9999999....9 = 9 * 10^(k-1) + 9 * 10^(k-2) + .... + 9 * 10^0  -  (1)
    9^2 * k = 9*9 * k  -  (2)
    
if divide both number by 9,
    (1) : 10^(k-1) + 10^(k-2) + ... + 10^0
    (2) : 9 * k
    
and we claim that (1) > (2), so every one step of 'square-sum' we do, the number is shrunk.
see :
    10^(k-1) + 10^(k-2) + ... + 10^0  >  10 * k  >  9 * k
    
this is true for k >= 3 because:
    (a) 10 * k  >  9 * k (true)
    (b) 10^(k-1) + 10^(k-2) + ... + 10^0  >  10 * k (true for k >=3)

for (b), refer below:

    10^(k-1) + 10^(k-2) + ... + 10^0  >  10^(k-1)
    and
    10^(k-1) > 10 * k for k >= 3
    
thus, by doing square-sum for arbitrary number n > 100,
this number will be shrunk into < 100.

after the number is shrunk into 2-order number (<100),
check if the combination of two digit is happy number or not.

'''


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        happy_hash = {
            (0,1): True, (1,0): True,
            (0,7): True, (7,0): True,
            (1,3): True, (3,1): True,
            (1,9): True, (9,1): True,
            (2,3): True, (3,2): True,
            (2,8): True, (8,2): True,
            (4,4): True,
            (4,9): True, (9,4): True,
            (6,8): True, (8,6): True,
            (7,9): True, (9,7): True
        }

        while True:
            temp = 0
            while n != 0:
                temp += (n % 10) ** 2
                n //= 10
            n = temp

            if n < 100:
                a = n % 10
                b = n // 10

                if (a,b) in happy_hash:
                    return True
                else:
                    return False



obj = Solution()
n = 132
print(obj.isHappy(n))

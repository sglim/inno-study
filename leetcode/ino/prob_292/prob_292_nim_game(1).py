'''
point is if number of stone is multiple of 4, user must be lose.
here is why:

n : description
1 : user win
2 : user win
3 : user win
4 : user lose -competitor always takes last stones
5 : if user takes 1 stone, win (4 stone for competitor) thus who got 5 stone will win (user win)
6 : if user takes 2 stone, win
7 : if user takes 3 stone, win
8 : as we see, range [5, 7] stones 'win range'. However user cannot prevent competitor falls into that range (user lose)

...

same pattern will appear every 4 times of stone number.
thus we can claim, if number of stone is multiple of 4, user will lose
'''


class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False

        if n % 4 == 0:
            return False

        return True
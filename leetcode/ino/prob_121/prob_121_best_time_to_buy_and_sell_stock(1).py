class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) <= 1:
            return 0

        max_idx = 1
        min_idx = 0
        min_candidate_idx = 0
        profit = prices[max_idx] - prices[min_idx]

        for idx in range(1, len(prices)):
            if prices[idx] > prices[max_idx]:
                max_idx = idx
                if profit < (prices[max_idx] - prices[min_candidate_idx]):
                    min_idx = min_candidate_idx

                profit = prices[max_idx] - prices[min_idx]
                print('*** :', profit)

            if prices[idx] < prices[min_idx]:
                min_candidate_idx = idx

        if profit < 0:
            profit = 0

        return profit


sol = Solution()
test_arr = [2,1,2,1,0,1,2]
print(sol.maxProfit(test_arr))
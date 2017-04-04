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
            if profit < (prices[idx] - prices[min_candidate_idx]):
                max_idx = idx
                min_idx = min_candidate_idx
                profit = prices[max_idx] - prices[min_idx]

            if prices[idx] < prices[min_candidate_idx]:
                min_candidate_idx = idx

            print('* cur idx :', idx, '/ min idx :', min_idx, '/ max idx :', max_idx, '/ min_candidate :', min_candidate_idx, '/ profit :', profit)

        if profit < 0:
            profit = 0

        return profit


sol = Solution()
# test_arr = [3, 3, 5, 0, 0, 3, 1, 4]  # 4
# test_arr = [7, 6, 4, 3, 1]  # 0
# test_arr = [2, 1, 2, 1, 0, 1, 2]  # 2
# test_arr = [7, 1, 5, 3, 6, 4]  # 5
test_arr = [4, 7, 1, 2, 11]  # 10
print(sol.maxProfit(test_arr))
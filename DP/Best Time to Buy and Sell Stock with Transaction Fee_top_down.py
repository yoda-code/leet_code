class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        end = len(prices)
        dp = {}

        def maxProfitSol(i, is_buy, k):

            if i == end:
                return 0

            if (i, k, is_buy) in dp:
                return dp[(i, k, is_buy)]

            if is_buy:
                local_max = max(-prices[i] + maxProfitSol(i + 1, 0, k), maxProfitSol(i + 1, 1, k))

            else:
                local_max = max(prices[i] - k + maxProfitSol(i + 1, 1, k), maxProfitSol(i + 1, 0, k))

            dp.update({(i, k, is_buy): local_max})

            return local_max

        return maxProfitSol(0, 1, fee)
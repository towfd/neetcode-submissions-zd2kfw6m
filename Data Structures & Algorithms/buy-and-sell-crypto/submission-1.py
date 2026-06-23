class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 暴力破解 每個數都跑一次迴圈
        # 若大於等於就不算 算小於的就好
        # 回傳最大值
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if i == j:
                    continue
                if prices[i] >= prices[j]:
                    continue
                profit = prices[j] - prices[i]
                if max_profit < profit:
                    max_profit = profit

        return max_profit
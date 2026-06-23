class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP解法
        # 建立兩個陣列 一個計算左邊過來最小，一個計算右邊過來最大
        # 根據這兩個陣列 取出最大的值
        n = len(prices)
        lprice = [0] * n
        rprice = [0] * n
        max_price = 0

        lprice[0] = prices[0]
        for i in range(1, n):
            lprice[i] = min(lprice[i - 1], prices[i])

        rprice[n - 1] = prices[n - 1]
        for i in range(n - 2, -1, -1):
            rprice[i] = max(rprice[i + 1], prices[i])
        
        for i in range(n):
            max_price = max(max_price, rprice[i] - lprice[i])
        return max_price
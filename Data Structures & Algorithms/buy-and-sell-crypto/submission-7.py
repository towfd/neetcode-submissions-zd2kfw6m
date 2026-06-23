class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 單次迴圈解法
        # 邊走邊紀錄目前歷史最低價，跑一個迴圈 將歷史最低價與目前最高價去做相減
        # 回傳最大值

        if not prices:
            return 0

        min_price = float('inf')
        max_price = 0
        for price in prices:
            min_price = min(price, min_price)
            current_price = price - min_price
            max_price = max(max_price, current_price)
        return max_price
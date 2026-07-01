class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 將空間複雜度降到O(1)
        # 從最後一天開始往回看
        # 每次紀錄最熱的那天
        # 若今天沒有比最熱那天還要熱，去看明天的溫度，若明天溫度沒有比較熱，就去看明天對應到最熱的那天，紀錄起來即可
        # 時間複雜度O(n)
        # 空間複雜度O(1)

        result_list = [0] * len(temperatures)
        hottest = 0
        for i in range(len(temperatures) - 1, -1, -1):
            current_temp = temperatures[i]
            if current_temp >= hottest:
                hottest = current_temp
                continue

            days = 1
            while temperatures[i + days] <= current_temp:
                days += result_list[i + days]

            result_list[i] = days

        return result_list        
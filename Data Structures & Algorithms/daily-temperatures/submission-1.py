class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 建立一個stack，裡面放等待未來溫暖天氣的索引
        # 規則如下，若今天的溫度比stack裡面的寒冷，放進去
        # 如果今天比stack裡面的溫熱，將裡面的值pop出來並計算天數塞入答案陣列
        # 時間複雜度O(n)
        # 空間複雜度O(n)

        tem_stack = []
        result_list = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while tem_stack and temperatures[tem_stack[-1]] < temperatures[i]:
                tem_idx = tem_stack.pop()
                result_list[tem_idx] = i - tem_idx
            tem_stack.append(i)
        return result_list
        
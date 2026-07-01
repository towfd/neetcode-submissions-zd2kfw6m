class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 暴力破解，遞迴去運算，若這次的數字比未來的小，就將index記錄下來，否則紀錄0
        # 時間複雜度O(N^2)
        # 空間複雜度O(N)

        result_list = [0] * (len(temperatures))
        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result_list[i] = (j - i)
                    break
        return result_list
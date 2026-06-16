class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 暴力破解
        # 使用兩個迴圈，每次比較不同值乘出來的大小
        # 回傳最大的值
        # 時間複雜度 O(N ^ 2)
        # 空間複雜度 O(1)

        maximun = 0
        for index1 in range(len(heights)):
            for index2 in range(index1, len(heights)):
                num = min(heights[index1], heights[index2]) * (index2 - index1)
                if maximun < num:
                    maximun = num
        return maximun
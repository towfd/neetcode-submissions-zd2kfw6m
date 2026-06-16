class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 給定兩個指標，一個指標從頭開始，另外一個從尾端開始
        # 每次比對大小，比對完畢後，僅需要移動較小的那個數值的指標即可
        # 時間複雜度 O(n)
        # 空間複雜度 O(1)
        index1, index2 = 0, len(heights) - 1
        maximum = 0
        while index1 < index2:
            total = min(heights[index1], heights[index2]) * (index2 - index1)
            if maximum < total:
                maximum = total
            if heights[index1] < heights[index2]:
                index1 += 1
            else:
                index2 -= 1
        return maximum
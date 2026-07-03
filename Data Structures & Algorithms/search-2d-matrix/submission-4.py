class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 將2維矩陣展平進行Binary Search
        # 這邊可以將用簡單的數學公式去將目前index對應到的二維矩陣位子找出來
        # 例如說 今天我們二維矩陣是 4 * 5 的矩陣，在這邊我們的middle是 10
        # 可以去計算對應的row 跟 col在哪 
        # row = middle // n(每個矩陣內元素數量) -> 10 // 5 = 2
        # col = middle % n -> 10 % 5 = 0
        # 就可以對應到 matrix[2][0] 的這個位子
        # 用binary search 下去跑直到找到答案為止
        # 時間複雜度O(log(m * n))
        # 空間複雜度O(1)
        
        n = len(matrix[0])
        l_idx, r_idx = 0, len(matrix) * n - 1
        while l_idx <= r_idx:
            middle = (l_idx + r_idx) // 2
            row = middle // n
            col = middle % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r_idx = middle - 1
            else:
                l_idx = middle + 1
        return False
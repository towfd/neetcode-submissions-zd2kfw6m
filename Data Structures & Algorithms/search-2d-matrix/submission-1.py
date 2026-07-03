class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 暴力破解
        # 對每個陣列去做binary search
        # 時間複雜度 O(m * log(n))
        # 空間複雜度 O(1)

        for nums in matrix:
            l_idx, r_idx = 0, len(nums) - 1
            while l_idx <= r_idx:
                middle = (l_idx + r_idx) // 2
                if nums[middle] == target:
                    return True
                elif nums[middle] > target:
                    r_idx = middle - 1
                else:
                    l_idx = middle + 1
        return False


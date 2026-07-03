class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 去Binary Search每個陣列的頭尾，去判斷target落在哪個區域
        # 對於目標陣列在進行一次binary search
        # 時間複雜度O(log(m * n))
        # 空間複雜度O(1)

        l_idx, r_idx = 0, len(matrix) - 1
        while l_idx <= r_idx:
            middle = (l_idx + r_idx) // 2
            if matrix[middle][0] <= target and matrix[middle][-1] >= target:
                nums = matrix[middle]
                ll_idx, rr_idx = 0, len(nums) - 1
                while ll_idx <= rr_idx:
                    n_middle = (ll_idx + rr_idx) // 2
                    if nums[n_middle] == target:
                        return True
                    elif nums[n_middle] > target:
                        rr_idx = n_middle - 1
                    else:
                        ll_idx = n_middle + 1
                return False
            elif matrix[middle][0] > target:
                r_idx = middle - 1
            else:
                l_idx = middle + 1
        return False
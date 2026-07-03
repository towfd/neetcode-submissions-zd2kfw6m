class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 由於已經是排序好的
        # 我們可以從最中間開始找
        # 如果中間 > target 往左邊找，反之，直到搜尋到為止，否則返回-1
        # 時間複雜度O(logn)
        # 空間複雜度O(1)
        l_idx, r_idx = 0, len(nums) - 1
        while l_idx <= r_idx:
            middle = (l_idx + r_idx) // 2
            if nums[middle] > target:
                r_idx = middle - 1
            elif nums[middle] < target:
                l_idx = middle + 1
            else:
                return middle
        return -1
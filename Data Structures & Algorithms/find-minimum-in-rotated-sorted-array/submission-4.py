class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 使用binary search
        # 直接去找中間的值，如果中間的值比最右邊的值大，代表他旋轉過了，所以推斷最小值在右邊
        # 如果沒有比右邊大，繼續往左邊找
        # 直到兩個指標相交為止
        # 時間複雜度O(logn)
        # 空間複雜度O(1)
        l_idx, r_idx = 0, len(nums) - 1
        while l_idx < r_idx:
            mid_idx = (l_idx + r_idx) // 2
            if nums[mid_idx] > nums[r_idx]:
                l_idx = mid_idx + 1
            else:
                r_idx = mid_idx
        return nums[l_idx]
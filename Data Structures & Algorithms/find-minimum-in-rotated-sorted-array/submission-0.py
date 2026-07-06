class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 使用binary search
        # 先將第一個數當作是最小數
        # 建立左右雙指標，去看中間的數是否小於第一個數
        # 如果找到小於的，往左邊找是否有更小的，如果大於的話，往右邊找是否有小於的
        # 直到兩個指標相碰為止結束尋找 返回最小值
        # 時間複雜度O(logn)
        # 空間複雜度O(1)
        min_num = nums[0]
        l_idx, r_idx = 1, len(nums) - 1
        while l_idx <= r_idx:
            mid_idx = (l_idx + r_idx) // 2
            if nums[mid_idx] < min_num:
                min_num = nums[mid_idx]
                r_idx = mid_idx - 1
            else:
                l_idx = mid_idx + 1
        return min_num
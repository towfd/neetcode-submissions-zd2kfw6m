class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 先判斷哪一半邊是遞增
        # 若 nums[mid] <= nums[r_idx]，代表右半邊是遞增的
        #   -> 若 target 剛好被夾在這個右半邊的範圍內，左指標往右縮 (往右找)
        #   -> 反之，代表 target 藏在左半邊，右指標往左縮
        # 若 nums[mid] > nums[r_idx]，代表左半邊是遞增的
        #   -> 若 target 剛好被夾在這個左半邊的範圍內，右指標往左縮 (往左找)
        #   -> 反之，代表 target 藏在右半邊，左指標往右縮
        # 找到就回傳 index，若直到左右指標相碰都沒有找到值，則回傳 -1
        # 時間複雜度O(logn)
        # 空間複雜度O(1)

        l_idx, r_idx = 0, len(nums) - 1
        while l_idx <= r_idx:
            mid = (r_idx + l_idx) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] <= nums[r_idx]:
                if nums[mid] < target <= nums[r_idx]:
                    l_idx = mid + 1
                else:
                    r_idx = mid - 1
            else:
                if nums[l_idx] <= target < nums[mid]:
                    r_idx = mid - 1
                else:
                    l_idx = mid + 1
        return -1




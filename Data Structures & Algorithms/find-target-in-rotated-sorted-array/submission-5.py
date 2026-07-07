class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 先搜尋最小值在哪
        # 依照這個最小值去找要從哪裡開始找
        # 做最後面用最基本的binary search找就可以
        l_idx, r_idx = 0, len(nums) - 1
        while l_idx < r_idx:
            mid = (l_idx + r_idx) // 2
            if nums[r_idx] < nums[mid]:
                l_idx = mid + 1
            else:
                r_idx = mid
        
        pivot = l_idx

        l_idx, r_idx = 0, len(nums) - 1
        if pivot > 0:
            if nums[pivot] <= target <= nums[r_idx]:
                l_idx = pivot
            else:
                r_idx = pivot - 1

        while l_idx <= r_idx:
            mid = (l_idx + r_idx) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l_idx = mid + 1
            else:
                r_idx = mid - 1
        return -1
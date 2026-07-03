class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 暴力破解
        # 建立兩個指標，一左一右，直到left > right
        # 找到就return index 沒找到就return -1
        # 時間複雜度O(n)
        # 空間複雜度O(1)

        l_idx, r_idx = 0, len(nums) - 1

        while l_idx <= r_idx:
            if nums[l_idx] == target:
                return l_idx
            elif nums[r_idx] == target:
                return r_idx
            
            l_idx += 1
            r_idx -= 1
        return -1

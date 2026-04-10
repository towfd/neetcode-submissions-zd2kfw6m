class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        max_len = 0
        current_len = 1
        if not nums:
            return 0
        for index in range(len(nums) - 1):
            diff = nums[index + 1] - nums[index]
            if diff == 0:
                continue
            elif diff == 1:
                current_len += 1
            else:
                if max_len <= current_len:
                    max_len = current_len
                current_len = 1
        if current_len >= max_len:
            max_len = current_len
        return max_len
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 建立兩個指標，指標距離設定為k
        # 建立一個答案陣列
        # 每次將最大值放入陣列中，直到右指標結束
        if len(nums) == 1:
            return nums
        output_list = []
        for r_idx in range(k - 1, len(nums)):
            l_idx = r_idx - (k - 1)
            r = max(nums[l_idx: r_idx + 1])
            print(r)
            output_list.append(max(nums[l_idx: r_idx + 1]))
        return output_list


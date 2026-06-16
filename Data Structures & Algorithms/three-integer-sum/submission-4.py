class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 降維打擊
        # 跑一個for迴圈，固定一個指標
        # 在裡面建立兩個指標，這兩個指標一個從左跑，一個從右跑，目的要找出相加後跟第一個指標為0的兩個數
        # 要注意去重複 要判斷index1 跟 index2是否跟前一個數字一樣 是的話就跳過
        # 時間複雜度為O(n ^ 2)
        # 空間複雜度為O(1) 回傳陣列不算
        ans = []
        nums.sort()
        for index1 in range(len(nums) - 2):
            if (index1 > 0) and (nums[index1] == nums[index1 - 1]):
                continue

            index2, index3 = index1 + 1, len(nums) - 1
            while index2 < index3:
                total = nums[index2] + nums[index3] + nums[index1]
                if total < 0:
                    index2 += 1
                elif total > 0:
                    index3 -= 1
                elif total == 0:
                    ans.append([nums[index2], nums[index3], nums[index1]])
                    index2 += 1
                    index3 -= 1
                    while index2 < index3 and (nums[index2] == nums[index2 - 1]):
                        index2 += 1
        return ans
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_list = []
        right_list = []
        result_list = []
        left_product = 1
        right_product = 1
        for index in range(len(nums)):
            if index - 1 < 0:
                num = 1
            else:
                num = nums[index - 1]
            left_product *= num
            left_list.append(left_product)

        for index in range(len(nums) - 1, -1 , -1):
            if index + 1 > len(nums) - 1:
                num = 1
            else:
                num = nums[index + 1]
            right_product *= num
            right_list.insert(0, right_product)


        for index in range(len(nums)):
            result_list.append(left_list[index] * right_list[index])
            
        return result_list
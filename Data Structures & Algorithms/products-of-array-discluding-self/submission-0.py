class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute solution
        # iterate the nums list 
        # product all the elements except the current index
        # rescord to the new array
        result_list = []
        for index, num in enumerate(nums):
            product_result = 1
            for s_index, s_num in enumerate(nums):
                if index == s_index:
                    continue
                product_result *= s_num
            result_list.append(product_result)
        return result_list
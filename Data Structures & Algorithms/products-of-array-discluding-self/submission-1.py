class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute-force Approach
        # For each element in the array, we calculate the product of all other elements.
        # We achieve this by using nested loops: the outer loop selects the current element to exclude,
        # and the inner loop multiplies all the other elements together.
        
        # Time Complexity: O(N^2), where N is the length of 'nums'. The nested loops cause 
        # the number of operations to grow quadratically.
        # Space Complexity: O(N) or O(1) auxiliary space, as 'result_list' is used to store 
        # the output and we don't use any other extra space.
        
        result_list = []
        for index, num in enumerate(nums):
            product_result = 1
            for s_index, s_num in enumerate(nums):
                # Skip the current index to calculate the product of the REST of the elements
                if index == s_index:
                    continue
                product_result *= s_num
            result_list.append(product_result)
            
        return result_list
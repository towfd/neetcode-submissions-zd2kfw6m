class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculates the product of all elements in the array except self.
        
        This algorithm uses the prefix and suffix product technique to achieve O(N) 
        time complexity without utilizing the division operation.
        
        Time Complexity: O(N), where N is the length of nums.
        Space Complexity: O(N), for storing the prefix and suffix product arrays.
        """
        n = len(nums)
        
        # Pre-allocate arrays to optimize memory allocation and avoid O(N) insertion costs
        left_list = [1] * n
        right_list = [1] * n
        result_list = [1] * n
        
        # Compute prefix products: product of all elements to the left of index 'i'
        for i in range(1, n):
            left_list[i] = left_list[i - 1] * nums[i - 1]
            
        # Compute suffix products: product of all elements to the right of index 'i'
        for i in range(n - 2, -1, -1):
            right_list[i] = right_list[i + 1] * nums[i + 1]
            
        # Combine prefix and suffix products to form the final result
        for i in range(n):
            result_list[i] = left_list[i] * right_list[i]
            
        return result_list
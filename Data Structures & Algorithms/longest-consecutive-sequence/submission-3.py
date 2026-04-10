class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute Force / Sorting Approach
        # First, sort the array.
        # Second, check if the array is empty. If it is empty, then return 0.
        # Third, initialize two variables to track the lengths:
        # one is the global max length, and the other is the current length.
        
        # Start iterating and calculate the difference between adjacent elements.
        # If the diff equals 0 (duplicate), then continue.
        # Else if the diff equals 1 (consecutive), increment current_len by 1.
        # Else (sequence broken), we check if the global max length <= current length, and update it if true.
        # Then reset the current length back to the default value (1).
        
        # In the end, we do one last comparison to check if the final current_len is larger than max_len.
        # Return the result.
        
        # Time Complexity: O(n log n). Sorting takes O(n log n) time and the iteration takes O(n) time.
        # Space Complexity: O(n) because the 'sorted()' function creates a new list. 
        # (Note: It would be O(1) auxiliary space if we used 'nums.sort()' for in-place sorting).
        
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
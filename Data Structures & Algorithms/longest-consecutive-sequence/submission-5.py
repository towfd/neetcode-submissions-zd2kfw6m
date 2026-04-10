class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # optimal solution
        # First, Check if the array is empty if is empty then return 0
        # Second, turn the nums array into a hash set for O(1) lookup time
        # Third, give a parameter to store the global max length
        # Start iterate the set to find the sequence
        # if the current number minus 1 is in the set, then continue (it is not the start)
        # else it means we find the start of a sequence, give a parameter to record current length
        # use a while loop to check if current number plus 1 is in the set
        # if it is inside, current_len += 1 and update current number
        # in the end of the while loop we compare the global max length, if the global max length <= current length, record current length
        # return the result
        
        # The time complexity, turn array into set cost O(n) times, and the while loop only run when we find the start of a sequence, so every number is visited at most twice. Overall it cost O(n).
        # The space complexity is O(n) where we use a set to store all the numbers.
        
        if not nums:
            return 0
            
        num_set = set(nums)
        max_len = 0
        
        for num in num_set:
            # Check if this number is the start of a sequence
            if (num - 1) not in num_set:
                current_num = num
                current_len = 1
                
                # keep finding the next consecutive number
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_len += 1
                    
                # update the global max length
                if max_len <= current_len:
                    max_len = current_len
                    
        return max_len
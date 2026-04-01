class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Approach: Iterative Search (Modified Brute Force)
        # 1. Find the smallest unprocessed number and calculate its complement (target - num).
        # 2. Scan the remaining elements in the array to find the complement.
        # 3. Repeat this process until a valid pair is found.
        # Time Complexity: O(N^2). In the worst case, we scan the array repeatedly for each element.
        # Space Complexity: O(N). The 'used_set' stores up to N visited indices.
        target_list = []
        smallest_index = 0
        used_set = set()
        while True:
            smallest_num = 100000000
            for i, num in enumerate(nums):
                #finding the smallest number
                if i not in used_set:
                    if smallest_num > num:
                        smallest_num = num
                        smallest_index = i

            next_target = target - smallest_num
            for i, num in enumerate(nums):
                if i == smallest_index:
                    continue
                if num == next_target:
                    target_list.append(smallest_index)
                    target_list.append(i)
                    break
            used_set.add(smallest_index)
            if target_list:
                break
        target_list = sorted(target_list)

        return target_list
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute 
        # finding the smallest number, then let target - smaller number
        # check the result is in the list, if not, then take the next
        # number until loop all the list, after find the number, check
        # the index in the list, then return the result
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
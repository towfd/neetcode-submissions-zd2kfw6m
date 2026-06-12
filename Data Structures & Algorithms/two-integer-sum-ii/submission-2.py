class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1, index2 = 0, 0
        while index1 != len(numbers):
            index2 = index1 + 1
            number = numbers[index1]
            next_target = target - number
            while index2 != len(numbers):
                if numbers[index2] == next_target:
                    return [index1 + 1, index2 + 1]
                index2 += 1
            index1 += 1
        return [index1 + 1, index2 + 1]

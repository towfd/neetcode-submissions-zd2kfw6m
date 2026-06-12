class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 給兩個指標，第一個指標會先跟target做相減，第二個指標會從index1的後面去尋找此list內是否有這個數字
        # 成立回傳True，否則繼續往前，直到index == len(list) - 1 回傳False
        # 時間複雜度為 N ^ 2 ，N為List的長度
        index1, index2 = 0, 0
        while index1 != len(numbers):
            number = numbers[index1]
            next_target = target - number
            if next_target in numbers[index1:]:
                index2 = numbers.index(next_target)
                return [index1 + 1 , index2 + 1]

            index1 += 1
        return [0, 0]

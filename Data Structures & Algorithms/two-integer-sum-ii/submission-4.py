class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 利用兩個指針，這邊可以讓index1初始在最左邊，index2初始在最右邊
        # 判斷 numbers[index1] + numbers[index2]的數值
        # 由於已經排序好的關係，最左邊必定為最小，最右邊必定為最大
        # 若數值太大，代表index2太右邊，將其 -1
        # 若數值太小，代表index1太左邊，將其 +1
        # 循序直到找到值
        # 時間複雜度從O(N ^ 2) 降為 O(N)
        # 空間複雜度 O(1)
        index1, index2 = 0, len(numbers) - 1
        while index1 < index2:
            count_number = numbers[index1] + numbers[index2]
            if count_number > target:
                index2 -= 1
            elif count_number < target:
                index1 += 1
            elif count_number == target:
                return [index1 + 1, index2 + 1] 
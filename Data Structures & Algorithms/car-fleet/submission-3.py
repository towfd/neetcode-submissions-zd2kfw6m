class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # bucket sort
        # 這招僅適用在記憶體不會爆炸的情況下，因為leetcode測試資料僅有百萬比，所以可以使用
        # 做法是target有多大就建立多少個bucket(所以在百萬級可以但是到千億級記憶體會炸裂)
        # 另外前提也是有說到位子不會重複，有重複要使用二維陣列做
        # 計算每台車到達的時間點，放入對應的bucket裡面
        # 從最後一個bucket開始往回看，並計算碰撞數量
        # 時間複雜度O(n + target)
        # 空間複雜度O(target)
        # 若是稀疏矩陣(車子很少但target超大)，會超級浪費空間
        target_bucket = [0.0] * target
        for pos, sp in zip(position, speed):
            target_bucket[pos] = (target - pos) / sp

        frontest_car_ari_time = 0.0
        car_fleet = 0

        for i in range(target - 1, -1, -1):
            cur_time = target_bucket[i]

            if cur_time > 0:
                if cur_time > frontest_car_ari_time:
                    frontest_car_ari_time = cur_time
                    car_fleet += 1
        return car_fleet
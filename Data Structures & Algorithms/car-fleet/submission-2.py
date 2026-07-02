class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 去排序position 從最大到最小
        # 去算出最前面那台車要到終點的時間
        # 紀錄目前最前面那台車到終點的時間，若後面的車在這個時間內，算同一個車隊
        # 直到後面的時間大於目前時間，更新時間 並將車隊 + 1
        cars = sorted(zip(position, speed))
        
        frontest_car_ari_time = 0
        car_fleet = 0
        for pos, sp in reversed(cars):
            cur_ari_time = (target - pos) / sp
            if cur_ari_time > frontest_car_ari_time:
                frontest_car_ari_time = cur_ari_time
                car_fleet += 1
        return car_fleet
# 车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）

# 给定整数 capacity 和一个数组 trips ,  trip[i] = [numPassengersi, fromi, toi] 表示第 i 次旅行有 numPassengersi 乘客，接他们和放他们的位置分别是 fromi 和 toi 。这些位置是从汽车的初始位置向东的公里数。

# 当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。


class Solution:
    def carPooling(self, trips, capacity) :
        # 扫一遍表，然后用额外的数组记录某个时间节点上下，求前缀和
        diff=[0]*1001
        for trip in trips:
            diff[trip[0]]+=trip[1]
            diff[trip[1]]-=trip[2]
        curcapacity=0
        for v in diff:
            curcapacity+=v
            if curcapacity>capacity:
                return False
        return True

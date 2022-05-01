from re import sub
from typing import  List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_sum=sum(gas)
        cost_sum=sum(cost)
        if cost_sum>gas_sum:
            return -1 
        sub_list=[ gas_x-cost[index] for index,gas_x in enumerate(gas)]
        start_index=0
        ans=0
        while start_index<len(sub_list):
            pre_index=(start_index-1)%len(sub_list)
            if sub_list[pre_index]<0 and sub_list[start_index]>=0:
                ans=start_index # 找到潜在的点了，然后向后计算是否能跑完全程？
                # 进行判断 是否满足条件， [start_index , start-1 ] 是否都是大于零，找到某个数index前面sub_list[index-1]<0 
                # 是的话，bingo
                index=start_index+1
                rest_gas=sub_list[start_index]
                while index<len(sub_list)+start_index:
                    rest_gas+=sub_list[index%len(sub_list)]
                    if rest_gas<0:
                        start_index=index+1
                        ans=-1
                        break
                    else:
                        index+=1
                if ans!=-1:
                    return ans
            start_index+=1
        return len(gas)-1
        
if __name__ == "__main__":
    instance=Solution()
    #instance.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2])
    instance.canCompleteCircuit(gas =[5,5,1,3,4], cost = [8,1,7,1,1])
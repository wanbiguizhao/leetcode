from functools import reduce


class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        # targetseconds x m y s  | x m y s y>60 
        def calculate_cost(minute,second):
            cost=0
            cur_startat=startAt
            time_list=[]
            if minute==0:
                if second>9:
                    time_list.append(second//10)
            elif minute<10:
                time_list.append(minute)
                time_list.append(second//10)
            else:
                time_list.append(minute//10)
                time_list.append(minute%10)

                time_list.append(second//10)
            time_list.append(second%10)
            for index,alphabet in enumerate(time_list):
                if alphabet!=cur_startat:
                    cost+=moveCost
                cost+=pushCost
                cur_startat=alphabet
            return cost
        target_list=[]
        x_minute=targetSeconds//60
        y_second=targetSeconds%60
        if x_minute>=100:
            target_list.append([x_minute-1,y_second+60])
        else:
            target_list.append([x_minute,y_second])
            if x_minute>=1 and y_second+60<100:
                target_list.append([x_minute-1,y_second+60])
        return min(calculate_cost(min,sec) for min,sec in target_list)

if __name__=="__main__":
    solution=Solution()
    # ans=solution.minCostSetTime( 1 ,1 , 10 ,60)
    # print(ans)
    # ans=solution.minCostSetTime( 1 ,100 , 10 ,60)
    # print(ans)
    # ans=solution.minCostSetTime( 0 ,1 , 4 ,9)
    # print(ans)
    # ans=solution.minCostSetTime( 7 , 220  , 479 ,6000)
    # print(ans)
    ans=solution.minCostSetTime( 1 ,2 , 1 , 600)
    print(ans)
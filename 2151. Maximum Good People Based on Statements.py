from doctest import FAIL_FAST
from os import stat
from typing import List 
class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        def check_ok(state):
            ok_flag=True 
            judge_list=[-1]*people_num
            for pi in range(people_num):
                pi_state=int(state>>pi)&1
                if pi_state==0:
                    continue
                for other_people in range(people_num):
                    if statements[pi][other_people]==2:
                        continue
                    if judge_list[other_people]==-1:
                        judge_list[other_people]=statements[pi][other_people]
                    elif judge_list[other_people]!=statements[pi][other_people]:
                        ok_flag=False 
                        return ok_flag 
            for i in range(people_num):
                t=int(state>>i)&1
                if (t==1 and judge_list[i]==0) or (t==0 and judge_list[i]==1):
                    ok_flag=False
                    return ok_flag
            return ok_flag 
        people_num=len(statements)
        for good_num in reversed(range(people_num+1)):
            state=2**good_num-1 # 总共有多少个人是真的。
            # Gosper's Hack是一种生成 [公式] 元集合所有 [公式] 元子集的算法，它巧妙地利用了位运算。这里我们先给出代码[1]
            while state<2**people_num:
                if check_ok(state):
                    return good_num 
                c = state& (- state)
                r = state + c
                state = int(((r ^ state) >> 2) / c)| r
        return 0
if __name__=="__main__":
    instance=Solution()
    ans=instance.maximumGood(statements =[[2,0,2,2,0],[2,2,2,1,2],[2,2,2,1,2],[1,2,0,2,2],[1,0,2,1,2]])

            

                

            

from typing import List 
class Solution:
    def maximumANDSum_2(self, nums: List[int], numSlots: int) -> int:
        # 状态压缩加 动态规划
        # 
        def find_jth_state(state_num,j):
            # j->[0,n]
            while j>0:
                state_num=state_num//3
                j-=1
            return state_num%3 
        const_num_len=len(nums)
        const_num_slots=numSlots
        all_state=3**const_num_slots
        #nums.insert(0,0)

        dp=[ [ 0 for s in  range(3**const_num_slots) ] for i in range(const_num_len+1) ]
        dp[0][0]=0
        for state in range(1,all_state):
            num_count=0
            tmp=state
            while tmp>0:
                num_count+=tmp%3
                tmp=tmp//3 
            # 记录大概用了多少个数字了。
            if num_count>const_num_len:
                continue
            for slot_th  in  range(const_num_slots):
                
                if (state//(3**slot_th))%3>0:
                    
                    pre_state=state-3**slot_th
                    dp[num_count][state]=max(dp[num_count-1][pre_state]+(nums[num_count-1]&(slot_th+1)),dp[num_count][state])
        return max(dp[const_num_len])
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        # 状态压缩,把所有的状态都弄出来
        # 
        const_num_len=len(nums)
        const_num_slots=numSlots
        all_state=3**const_num_slots
        #nums.insert(0,0)

        dp=[0]*(all_state+1)
        dp[0]=0
        for state in range(1,all_state):
            num_count=0
            tmp=state
            while tmp>0:
                num_count+=tmp%3
                tmp=tmp//3 
            # 记录大概用了多少个数字了。
            if num_count>const_num_len:
                continue
            for slot_th  in  range(const_num_slots):
                
                if (state//(3**slot_th))%3>0:
                    
                    pre_state=state-3**slot_th
                    dp[state]=max(dp[pre_state]+(nums[num_count-1]&(slot_th+1)),dp[state])
        return max(dp)
if __name__=="__main__":
    solution=Solution()
    ans=solution.maximumANDSum(nums = [1,2,3,4,5,6], numSlots = 3)
    print(ans )
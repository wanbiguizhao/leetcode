from functools import reduce
class Solution:
    def minimumTime2(self, s: str) -> int:
        # 动态规划的方案
        const_s_len=len(s)
        dp_pre= [2*const_s_len]*(const_s_len+2) # for rule 1 and 3 [1,i] min remove cost 
        dp_post=[2*const_s_len]*(const_s_len+2) # for rule 2 and  [i+1,n] min remove cost 
        dp_pre[0]=0
        dp_post[const_s_len]=0
        ans=2*const_s_len
        for index in range(1,const_s_len+1):
            if s[index-1]=="1":
                dp_pre[index]=min(dp_pre[index-1]+2,index)
            else:
                dp_pre[index]=dp_pre[index-1]
        dp_post[const_s_len]=0
        s_th=const_s_len-1
        while s_th>=0:
            index=s_th
            if s[index]=="1":
                dp_post[s_th]=min(dp_post[s_th+1]+2,const_s_len-s_th)
            else:
                dp_post[s_th]=dp_post[s_th+1]
            s_th=s_th-1
        ans=min(map( lambda z: z[0]+z[1],zip(dp_pre,dp_post)))
        ans=min(ans,const_s_len)
        return ans 
    def minimumTime(self, s: str) -> int:
        # 前缀和 pre_sum
        #  [0,i] 移出， [j+1,n] 移出， [i+1,j] 做改变。
        # [0,i] 代表的代价为  i 
        # [j+1,n] 代表的开销为 n-j-1+1= n-j
        # [i+1,j] 代表开销为 2x( pre_sum[j]-pre_sum[i] ) 表示整体有1的情况。
        # 求min:   n+(2pre_sum[j]-j)-(2pre_sum[i]-i) 的最小值
        # 表示 从pre_sum中找到(i,j) 是的 n+ (2pre_sum[j]-j)-(2pre_sum[i]-i) 最小
        const_s_len=len(s)
        pre_sum=[0]*(const_s_len+1)
        s_th=1
        while s_th<=const_s_len: 
            pre_sum[s_th]=pre_sum[s_th-1]+ 1 if s[s_th-1] =="1" else pre_sum[s_th-1]
            s_th+=1
        cost_i=0 # 重点
        cost_j=cost_i
        min_cost=const_s_len
        for j_th in range(1,const_s_len+1): # 重点
            cost_j=2*pre_sum[j_th]-j_th
            min_cost=min(min_cost,cost_j-cost_i+const_s_len)
            cost_i=max(cost_i,cost_j)
        return min(min_cost,const_s_len)
            

if __name__=="__main__":
    solution=Solution()
    # ans=solution.minimumTime("1111")
    # print(ans)
    # ans=solution.minimumTime("111000")
    # print(ans)
    # ans=solution.minimumTime("00011")
    # print(ans     )
    # ans=solution.minimumTime("1010101")
    # print(ans     )
    ans=solution.minimumTime("""0010""")
    print(ans     )
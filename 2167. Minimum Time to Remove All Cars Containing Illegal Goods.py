from functools import reduce
class Solution:
    def minimumTime(self, s: str) -> int:
        # 前缀和
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
        for s_th in reversed(range(0,const_s_len)):
            index=s_th
            if s[index]=="1":
                dp_post[s_th]=min(dp_post[s_th+1]+2,const_s_len-s_th)
            else:
                dp_post[s_th]=dp_post[s_th+1]
            ans=min(ans,dp_post[index]+dp_pre[index])
        
        return ans 

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
    ans=solution.minimumTime("""010110""")
    print(ans     )
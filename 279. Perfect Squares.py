class Solution:
    def numSquares(self, n: int) -> int:
        dp=[n+1]*(n+1)
        dp[0]=0
        dp[1]=1
        x=2
        while x<=n:
            i=1
            while i*i<=x:
                dp[x]=min(dp[x],1+dp[x-i*i])
                # 看看有没有办法做减枝头？
                i=i+1
            x+=1
        return dp[n]
                
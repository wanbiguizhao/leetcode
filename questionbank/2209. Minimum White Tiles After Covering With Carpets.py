import pysnooper


class Solution:
    @pysnooper.snoop()
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        dp=[ [0]*(numCarpets+1) for i in range(len(floor))]
        dp[0][0]=1 if floor[0]=="1" else 0
        for floor_ith,floor_ith_value in enumerate(floor):
            if floor_ith==0:
                continue
            for carpets_num in range(numCarpets+1):
                dp[floor_ith][carpets_num]=dp[floor_ith-1][carpets_num]
                if floor_ith_value=="1":
                    dp[floor_ith][carpets_num]+= 1
                if carpets_num>0:
                    if floor_ith<carpetLen:
                        dp[floor_ith][carpets_num]=0
                    else:
                        dp[floor_ith][carpets_num]=min(dp[floor_ith][carpets_num] ,dp[floor_ith-carpetLen][carpets_num-1])

                    

        return dp[len(floor)-1][-1]

if __name__=="__main__":
    instance=Solution()
    ans=instance.minimumWhiteTiles("10110101",2,2)
    print(ans)
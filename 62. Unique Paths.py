class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 数学题  m+n ，选择走m步之后，n步就确认了。
        # C (m+n) m
        # dp 题 问题可以转化为dp(m,n)=dp(m-1,n)+dp(m,n-1)
        def grid_traveller(m,n):
            if m==1 or n==1:
                return 1 
            if m==0 or n==0:
                return 0 
            memory[(m,n)]=grid_traveller(m-1,n)+grid_traveller(m,n-1)
            return memory[(m,n)]
        memory={}
        
        return grid_traveller(m,n)





if __name__ == "__main__":
    instance=Solution()
    print(instance.uniquePaths(1,1))
    print(instance.uniquePaths(2,1))
    print(instance.uniquePaths(2,2))
    print(instance.uniquePaths(3,2))
    print(instance.uniquePaths(3,7))
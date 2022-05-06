from doctest import FAIL_FAST


class Solution:
    def countPrimes(self, n: int) -> int:
        # https://leetcode.com/problems/count-primes/submissions/ 
        # 注意审题 ：Given an integer n, return the number of prime numbers that are strictly less than n.
        # n 只要不能被自己n^(1/2)整除，就是素数
        # 注意 1 不是素数   2 不是素数？
        
        is_primes=[True]*(n)
        for x in range(2,n):# 其实要看n-1
            if not is_primes[x]:# 不是素数就pass
                continue
            y=x*x 
            while y<n:
                is_primes[y]=False # 知道素数
                y+=x 
        ans=0
        for x in range(2,n):
            if is_primes[x]:
                ans+=1
        #print(ans)
        return ans 
    def countPrimes(self, n: int) -> int:
        is_primes=[True]*(n)
        for x in range(2,n):# 其实要看n-1
            if not is_primes[x]:# 不是素数就pass
                continue
            #y=x*x 
            for y in range(x*x,n,x): # 替代while的方法，也不是特别高效。
                is_primes[y]=False # 知道素数
                 
        ans=0
        for x in range(2,n):
            if is_primes[x]:
                ans+=1
        #print(ans)
        return ans 

if __name__=="__main__":
    instance=Solution()
    instance.countPrimes(2)
    instance.countPrimes(3)
    instance.countPrimes(5)
    instance.countPrimes(7)
    instance.countPrimes(15)


         
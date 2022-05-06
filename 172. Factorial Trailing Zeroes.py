class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0
        multiply_num=1
        for i in range(1,n+1):
            multiply_num=multiply_num*i
            while multiply_num%10==0:
                count+=1
                multiply_num=multiply_num//10
        print(n,count)
        return count 
    def trailingZeroes(self, n: int) -> int:
        # 考虑包含5的流程。
        # 25 这样的情况， 25=5^2 125=5^3 
        #11!=(2^8*5^2*) 看成5的指数，指数的值可以作为零的个数
        #   25=5^2 125=5^3  所以要一直做n=n//5的操作。

        count=0
        while n:
            count=n//5
            n=n//5
        return count 
if __name__ == "__main__":
    instance=Solution()
    instance.trailingZeroes(10)
    instance.trailingZeroes(50)
    instance.trailingZeroes(100)
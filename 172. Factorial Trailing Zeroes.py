from cv2 import divide


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
    def trailingZeroes(self, n: int) -> int:
        # 考虑包含5的流程。
        # 25 这样的情况， 25=5^2 125=5^3 
        #11!=(2^8*5^2*) 看成5的指数，指数的值可以作为零的个数
        #   25=5^2 125=5^3  所以要一直做n=n//5的操作。
        # 尝试使用reduce
        from functools import reduce
        divide_list=[0,5,5**2,5**3,5**4,5**5,5**6]
        def zeroes_helper(res,divid_num):
            res+=n//divid_num
            return res 
        ans=reduce(zeroes_helper,divide_list)
        print(ans)
        return ans 
if __name__ == "__main__":
    instance=Solution()
    instance.trailingZeroes(4)
    instance.trailingZeroes(5)
    instance.trailingZeroes(10)
    instance.trailingZeroes(50)
    instance.trailingZeroes(100)
    instance.trailingZeroes(100000)
from paddle import neg


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negitive_flag=False 
        if (dividend<0 and divisor>0)  or ( dividend>0 and divisor<0 ):
            negitive_flag=True 
    
        dividend=abs(dividend)
        divisor=abs(divisor)
        if dividend==0 or dividend< divisor:
            return 0
        register_sum=0
        register_ans=0
        ans=0

        while register_sum<dividend:
            register_sum+=divisor
            register_ans=ans 
            ans+=1
        if register_sum==dividend:
            if negitive_flag:
                return -ans
            return ans 
        if negitive_flag:
            return -register_ans
        return register_ans 
if __name__ == "__main__":
    instance = Solution()
    print(instance.divide(10,3))
    print(instance.divide(10,-3))
    print(instance.divide(10,-30))
    print(instance.divide(-30,-30))
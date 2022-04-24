from paddle import neg


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        max_num=2**31-1
        min_num=-2**31
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
        add_num=divisor
        divisor_count=1
        while register_sum<dividend :
            register_sum+=add_num
            register_ans=ans 
            ans+=divisor_count
            if register_sum>dividend : 
                if add_num==divisor:
                    break
                else:
                    register_sum=register_sum-add_num
                    ans=ans-divisor_count
                    add_num=divisor
                    divisor_count=1
            else:
                add_num=add_num+add_num
                divisor_count=divisor_count+divisor_count


        if register_sum==dividend:
            if negitive_flag:
                return max(-ans,min_num)
            return min(max_num,ans)
        if negitive_flag:
            return max(-ans+1,min_num)
        return min(ans-1,max_num) 
if __name__ == "__main__":
    instance = Solution()
    print(instance.divide(10,3))
    print(instance.divide(10,-3))
    print(instance.divide(10,-30))
    print(instance.divide(-30,-30))
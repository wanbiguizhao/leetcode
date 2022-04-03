class Solution:
    def countEven(self, num: int) -> int:
        def have_even_sum_digit(n):
            sum=0
            while n>0:
                sum+=n%10
                n=n//10
            return 1 if sum%2==0 else 0
        return sum(have_even_sum_digit(x) for x in range(1,num+1)) 
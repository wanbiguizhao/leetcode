


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1 
        if x==0:
            return 0
        if x==1:
            return x 
        if n<0:
            x=1/x
            n=-n
        ans=x 
        multiply_value=x # 记录每次递增的变量值
        multiply_n=1 # 记录每次递增的变量n
        current_n=1 # 
        while current_n<n:
            if current_n+multiply_n<n: # 迈大步，步长翻倍
                ans=ans*multiply_value
                current_n=current_n+multiply_n
                multiply_n=multiply_n*2
                multiply_value=multiply_value*multiply_value
            else: # 回退到最小的步长
                multiply_n=1
                multiply_value=x 
                ans=ans*multiply_value
                current_n=current_n+multiply_n  
        return ans
if __name__ == "__main__":
    instance=Solution()
    print(instance.myPow(0,1))
    print(instance.myPow(1,1))
    print(instance.myPow(2,1))
    print(instance.myPow(2,10))
    print(instance.myPow(2,-2))
    print(instance.myPow(4,-1))
    print(instance.myPow(-1/2,-9))

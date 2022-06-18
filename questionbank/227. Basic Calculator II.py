class Solution:
    def calculate(self, s: str) -> int:
        def _calculate(a,b,token): # 内部定义函数速度更快
            if token=="+":
                return a+b
            elif token=='-':
                return a-b
            elif token=="*":
                return a*b
            else:
                # if a*b<0:
                #     a=abs(a)
                #     b=abs(b)
                return int(a/b) # this is 向零取整 int，  round 四舍五入  ceil 向下取整， floor 是向上取整, int 是向零取整
                # import math 
                # math.in
        num_stack=[]
        siginal_stack=[]
        siginal_set=set(["+","/","-","*"])
        beg_index=0
        for index,x in enumerate(s):
            if x in siginal_set:
                siginal_stack.append(x)
                num_stack.append(int(s[beg_index:index]))
                beg_index=index+1
        num_stack.append(int(s[beg_index:]))
        while  siginal_stack:
            operate_symbol=siginal_stack.pop()
            b=num_stack.pop()
            a=num_stack.pop()
            ans=_calculate(a,b,operate_symbol)
            num_stack.append(ans)
        return num_stack[-1]
            

if __name__ == "__main__":
    instance=Solution()
    instance.calculate( s = "3+5/2")
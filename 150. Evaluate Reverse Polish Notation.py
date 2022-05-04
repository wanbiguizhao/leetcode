from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculate(a,b,token):
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
                return int(a/b) # this is 向零取整
                # import math 
                # math.in
        result_stack=[]
        for token in tokens:
            if token in ['+','-','*','/']:
                b=result_stack.pop(-1)
                a=result_stack.pop(-1) 
                c=calculate(a,b,token)
                result_stack.append(c)
            else:
                num=int(token)
                result_stack.append(num)
        print(result_stack[0])
        return result_stack[0]
if __name__ == "__main__":
    instance=Solution()
    #instance.evalRPN(tokens = ["2","1","+","3","*"])
    instance.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
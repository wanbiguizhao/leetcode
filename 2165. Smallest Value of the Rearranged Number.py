
from ntpath import join
from itsdangerous import json


class Solution:
    def smallestNumber(self, num: int) -> int:
        if num>= -10 and num <=10 :
            return num 
        if num<0:
            # do something 
            num=-num
            str_num=str(num)
            str_num="".join(sorted(str_num,reverse=True))
            return 0-int(str_num)
        str_num=str(num)
        zero_num=str_num.count('0')
        str_num="".join(sorted(str_num))
        return int(str_num[zero_num]+"0"*zero_num+str_num[zero_num+1:] )

if __name__=="__main__":
    solution=Solution()
    ans=solution.smallestNumber(0)
    print(ans,ans==0)
    ans=solution.smallestNumber(1300)
    print(ans,ans==1003)
    ans=solution.smallestNumber(-1300)
    print(ans,ans==-3100)
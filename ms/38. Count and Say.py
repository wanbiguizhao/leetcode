import re


class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n==1:
            return "1" 
        count=1
        say="1"
        while count<n:
            cnt=1
            num=say[0]
            presay=""
            index=1
            while index<len(say):
                if say[index]==say[index-1]:# 判断数组中两个字母是否一样，可以采用do while的方法，先检查之前的。
                    cnt+=1
                else:
                    presay=presay+str(cnt)+num
                    cnt=1
                    num=say[index]
                index+=1
            say=presay+str(cnt)+num
            count+=1
        return say

def testCase0(instance:Solution=Solution()):
    print(instance.countAndSay(2),"11")
    print(instance.countAndSay(3),"21")
    print(instance.countAndSay(4),"1211")


def wrongCase0(instance:Solution=Solution()):
    pass


if __name__ =="__main__":
    
    testCase0()

from typing import List
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #Q:
        # will negative number be appeared in the inputs ?
        # will number which contain any leading zero be appeared in the inputs？
        # intermediate result 中间结果
        def _multiply(AList:List[int],b:int)->str:
            if b==0:
                return "0"
            carryNum=0
            index=len(AList)-1
            ans=""
            while index>=0:
                x=AList[index]*b+carryNum
                carryNum=x//10
                x=x%10
                ans=str(x)+ans
                index-=1
            if carryNum>0:
                ans=str(carryNum)+ans
            return ans
        def numStrAdd(strA,strB):
            carryNum=0
            aIndex=len(strA)-1
            bIndex=len(strB)-1
            ans=""
            while aIndex>=0 and bIndex>=0:
                a=int(strA[aIndex])
                b=int(strB[bIndex])
                c=a+b+carryNum
                carryNum=c//10
                c=c%10
                ans=str(c)+ans
                aIndex-=1
                bIndex-=1
            while aIndex>=0:
                a=int(strA[aIndex])
                c=a+carryNum
                carryNum=c//10
                c=c%10
                ans=str(c)+ans
                aIndex-=1
            while bIndex>=0:
                b=int(strB[bIndex])
                c=b+carryNum
                carryNum=c//10
                c=c%10
                ans=str(c)+ans
                bIndex-=1
            if carryNum>0:
                ans=str(carryNum)+ans
            return ans 
        if len(num2)>len(num1):
            num1,num2=num2,num1
        elif len(num1)==len(num2) and num2>num1:
            num1,num2=num2,num1
        if num2=="0":
            return "0" 
        cache=[ _multiply(list(map(int,num1)),i) for i in range(10)]
        nums2Index=len(num2)-1
        lastResult=""
        while nums2Index>=0:
            x=num2[nums2Index]
            result=cache[int(x)]+"0"*(len(num2)-nums2Index-1)
            lastResult=numStrAdd(result,lastResult)
            nums2Index-=1
        return lastResult
def testCase0(instance=Solution()):
    res=instance.multiply(num1 = "2", num2 = "3")
    print(res,True)
    res=instance.multiply(num1 = "123", num2 = "456")
    print(res,True)
    res=instance.multiply(num1 = "123", num2 = "4567")
    print(res,True)
    res=instance.multiply(num1 = "0", num2 = "4567")
    print(res,True)
    res=instance.multiply(num1 = "2", num2 = "1000001")
    print(res,True)
def testCase0_wrong(instance=Solution()):
    # leetcode 没有通过的例子
    pass 
if __name__ =="__main__":
    testCase0()
    testCase0_wrong()
    
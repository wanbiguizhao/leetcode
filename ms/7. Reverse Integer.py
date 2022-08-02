from typing import List 

class Solution:
    def reverse(self, x: int) -> int:
        # leading zero question
        # negative flag question
        # 
        if x==0:
            return 0
        negBoundary=str(2**31)
        posBoundary=str(2**31-1)
        boundary=posBoundary
        negativeflag=False 
        if x<0:
            negativeflag=True 
            boundary=negBoundary
            x=-x
        strx=str(x)
        strx=strx[::-1]
        if len(strx)==len(boundary) and strx>boundary:
            return 0
        leadingZeroIndex=0
        while leadingZeroIndex <len(strx):
            if strx[leadingZeroIndex]==0:
                leadingZeroIndex+=1
            else:
                break
        if negativeflag:
            return -int(strx)#int("-{}".format(strx[leadingZeroIndex:]))
        return int(strx)

         



def testCase0(instance:Solution=Solution()):
    assert instance.reverse(0)==0
    assert instance.reverse(10)==1
    assert instance.reverse(2**31+1)==0
    assert instance.reverse(-2**31-1)==0
    assert instance.reverse(90000000)==9
    assert instance.reverse(-90000000)==-9

def wrongCase0(instance:Solution=Solution()):
    pass
if __name__ =="__main__":
    testCase0()
    wrongCase0()
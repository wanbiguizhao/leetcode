from typing import List 

class Solution:
    def reverse(self, x: int) -> int:
        # leading zero question
        # negative flag question
        # 
        if x==0:
            return 0
        #negBoundary=str(2**31)
        negBoundary="2147483648"
        #print(str(2**31))
        #posBoundary=str(2**31-1)
        posBoundary="2147483647"
        boundary=posBoundary
        negativeflag=False 
        if x<0:
            negativeflag=True 
            boundary=negBoundary
            x=-x
        strx=str(x)[::-1]
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
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        rev = 0
        while x != 0:
            # INT_MIN 也是一个负数，不能写成 rev < INT_MIN // 10
            if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
                return 0
            digit = x % 10
            # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
            if x < 0 and digit > 0:
                digit -= 10

            # 同理，Python3 的整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
            x = (x - digit) // 10
            rev = rev * 10 + digit
        
        return rev




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
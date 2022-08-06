

class Solution:
    def calculate(self, s: str) -> int:
        sigin=1
        ops=[1]
        ret=0
        index=0
        while index<len(s):
            if s[index]==" ":
                index+=1
            elif s[index]=="(":
                index+=1
                ops.append(sigin)
                
            elif s[index]=="+":
                index+=1
                sigin=ops[-1]
            elif s[index]=="-":
                index+=1
                sigin=-ops[-1]
            elif s[index]==")":
                # 回退堆栈里面的数字。
                ops.pop()
                index+=1
            else:
                num=0 
                while index <len(s)and s[index].isdigit():
                    num=num*10+int(s[index])
                    index+=1
                ret+=sigin*num
                
        return ret

def testCase0(instance:Solution=Solution()):
    assert instance.calculate("1+2+3")==6
    assert instance.calculate("-1+(2+3-(4+5))")==-5
def wrongCase0(instance:Solution=Solution()):
    assert instance.calculate("(7)-(0)+(4)")==11
if __name__ =="__main__":
    testCase0()
    wrongCase0()
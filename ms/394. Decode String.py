class Solution:
    def decodeString(self, s: str) -> str:
        # s会不会出现中括号不匹配的情况，
        # 是否会出现嵌套的情况？
        # square brackets 中括号
        # 递归，要不就是堆栈
        def _recDecodeString(begIndex,endIndex):
            kValue=0
            index=begIndex
            ans=""
            while index<endIndex:
                x=s[index]
                if x.isdigit():
                    kValue=kValue*10+int(x)
                    
                elif x=="[":
                    rightSquareBracktsIndex=squareBrackIndexCache[index] # 括号的范围。
                    begindex=index+1
                    substring=_recDecodeString(begindex,rightSquareBracktsIndex)
                    ans+=substring*kValue
                    kValue=0
                    index=rightSquareBracktsIndex
                else:
                    ans+=s[index]
                index=index+1
            return ans 
        # 记录一下square brackets stack 可以先记录上每个子问题的范围。
        squareBracketsStack=[]
        squareBrackIndexCache={}
        for index,x in enumerate(s):
            if x=="[":
                squareBracketsStack.append(index)
            elif x=="]":
                xindex=squareBracketsStack.pop(-1)
                squareBrackIndexCache[xindex]=index 
        ans=_recDecodeString(0,len(s))
        return ans 
def testCase0(instance:Solution=Solution()):
    # res=instance.reverseWords("    ")
    # print(res,res=="")
    # res=instance.reverseWords("    aaa   bb c")
    # print(res,res=="c bb aaa")
    res=instance.decodeString( "3[a]2[bc]")
    print(res,res=="aaabcbc")
    res=instance.decodeString( "3[a2[c]]2[bc]")
    print(res,res=="accaccaccbcbc")
if __name__ =="__main__":
    #testCase0()
    testCase0()
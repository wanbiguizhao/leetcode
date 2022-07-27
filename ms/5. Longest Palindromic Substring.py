class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 中心扩展法
        temp_str="#"+"#".join(list(s))+"#"
        ConstTempStrLength=len(temp_str)
        ansBegIndex=0
        ansEndIndex=-1
        for index in range(ConstTempStrLength):
            beg=index-1
            end=index+1
            while beg>=0 and end<ConstTempStrLength and temp_str[beg]==temp_str[end]:
                if ansEndIndex-ansBegIndex<end-beg:
                    ansEndIndex,ansBegIndex=end,beg
                beg-=1
                end+=1
        return s[ansBegIndex//2:ansEndIndex//2]

    def longestPalindrome(self, s: str) -> str:
        # 中心扩展法，不使用外部空间
        def palindrome(beg,end):
            ansBeg=beg
            ansEnd=beg
            while end< constLenOfS and beg>=0 and s[beg]==s[end]:
                if ansEnd-ansBeg<end-beg:
                    ansEnd,ansBeg=end,beg
                beg-=1
                end+=1
            return ansBeg,ansEnd
        constLenOfS=len(s)
        resBeg,resEnd=0,0
        for i in range(constLenOfS):
            beg,end=palindrome(i,i)
            if resEnd-resBeg<end-beg:
                resEnd,resBeg=end,beg 
            beg,end=palindrome(i,i+1)
            if resEnd-resBeg<end-beg:
                resEnd,resBeg=end,beg 
        return s[resBeg:resEnd+1]
def testCase0(instance:Solution=Solution()):
    res=instance.longestPalindrome("a")
    print(res,res=="a")
    res=instance.longestPalindrome("aab")
    print(res,res=="aa")
    res=instance.longestPalindrome("aba")
    print(res,res=="aba")
    res=instance.longestPalindrome("aa")
    print(res,res=="aa")
    res=instance.longestPalindrome("babad")
    print(res,res=="aba")



def wrongCase0(instance:Solution=Solution()):
    res=instance.longestPalindrome("cbbd")
    print(res,res=="bb")



if __name__ =="__main__":
    
    testCase0()
    wrongCase0()



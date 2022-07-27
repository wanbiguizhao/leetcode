class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s 
        temp_str="#"+"#".join(list(s))+"#"
        ans=0
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
    pass 



if __name__ =="__main__":
    
    testCase0()
    wrongCase0()



from collections import Counter 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s长度大概是多少？
        # s的字符组成都有哪些？
        # --------------
        # 双指针吧
        ans=0 
        if not s:
            return ans 
        ans=1 # 最少答案。
        begIndex=0# 代表着[begindex,len(s)-1]是可以搜索的区域。
        indexDict={} 
        for index,ch in enumerate(s):
            if ch in indexDict:
                begIndex=max(begIndex,indexDict[ch]+1) # 错误的地方
                indexDict[ch]=index
            else : 
                indexDict[ch]=index
            ans=max(ans,index-begIndex+1) # 每一步都检查一下。

        # 最后处理，非常重要。 
        return ans 
def testCase0(instance:Solution=Solution()):
    print(instance.lengthOfLongestSubstring("abcdefg"),7)
    print(instance.lengthOfLongestSubstring("abcabcdefg"),7)
    print(instance.lengthOfLongestSubstring("abcabcdefgap"),8)
    print(instance.lengthOfLongestSubstring("abcdefgabc"),7)
    print(instance.lengthOfLongestSubstring("g"),1)
    print(instance.lengthOfLongestSubstring("aaaaa"),1)

def wrongCase0(instance:Solution=Solution()):
    print(instance.lengthOfLongestSubstring("abcabcbb"),3)
    print(instance.lengthOfLongestSubstring("abba"),2)


if __name__ =="__main__":
    
    testCase0()
    wrongCase0()

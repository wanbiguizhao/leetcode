# 现场编程题题目内容：
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

# 示例 1:

# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:

# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

from bisect import bisect_left


def getXLongestSub(s:str):
    const_len=len(s)
    alphet_set=set()
    left=0
    right=0
    ans=0
    while right<const_len:
        if s[right] in alphet_set:
            while  s[left] !=s[right]:
                alphet_set.remove(s[left])
                left+=1
            left+=1
        else:
            alphet_set.add(s[right]) 
        ans=max(right-left+1,ans)
        right+=1
    return ans
# test case 01
if __name__=="__main__":
    assert getXLongestSub("a")==1
    print(getXLongestSub("aba"),2)
    assert getXLongestSub("abb")==2 # ？
    print( getXLongestSub("abbca"),3)
    print( getXLongestSub("aaaaaa"),1)
    print( getXLongestSub("abcabcbb"),3)
    # "pwwkew"
    print( getXLongestSub("pwwkew"))
    #assert getXLongestSub("abbca")==2 # ？

from bisect import bisect_left
bisect_left(range(max(100)),)
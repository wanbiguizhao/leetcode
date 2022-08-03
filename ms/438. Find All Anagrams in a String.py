from typing import List 
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # desc
        # ill use sliding windows which width is eqaul to the length of sring p 
        # progamer count each letter of s word or  word in the sliding windows
        # the number of each letter  between  words is completely constant
        ans=[]
        pCounter=Counter(p)
        constLenS=len(s)
        constLenP=len(p)
        index=0
        while index+constLenP<=constLenS:# < can not pass  wrongCase0
            counter=Counter(s[index:index+constLenP])
            if counter==pCounter:
                ans.append(index)
            index+=1
        return ans 
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len,p_len=len(s),len(p)
        
        if s_len<p_len:
            return [] 
        ans=[]
        count=[0]*26
        for i in range(p_len):
            count[ord(s[i])-ord('a')]+=1
            count[ord(p[i])-ord('a')]-=1
        differ=[ c!=0 for c in count].count(True)
        if differ==0:
            ans.append(0)
        for i in range(s_len-p_len):
            if count[ord(s[i])-ord('a')]==1:
                differ-=1
            elif count[ord(s[i])-ord('a')]==0:
                differ+=1
            count[ord(s[i])-ord('a')]-=1 
            if count[ord(s[i+p_len])-ord('a')]==-1:
                differ-=1
            elif count[ord(s[i+p_len])-ord('a')]==0:# pointer
                differ+=1
            count[ord(s[i+p_len])-ord('a')]+=1 
            if differ==0:
                ans.append(i+1)
        return ans 






def testCase0(instance:Solution=Solution()):
    assert [0,6]==instance.findAnagrams(s = "cbaebabacd", p = "abc")
def wrongCase0(instance:Solution=Solution()):
    assert [0,1,2]==instance.findAnagrams(s = "abab", p = "ab")
if __name__ =="__main__":
    testCase0()
    wrongCase0()

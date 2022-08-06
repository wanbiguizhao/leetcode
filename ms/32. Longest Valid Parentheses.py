from typing import List 

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # runtime complexty O(n)
        # space complexity O(1)
        ans=0
        left,right=0,0
        index=0
        sLen=len(s)
        while index<sLen:
            if s[index]=="(":
                left+=1
            else:
                right+=1 
            if left==right:
                ans=max(ans,left*2)
            elif left<right:
                left=right=0

            index+=1
        index=sLen-1
        left,right=0,0
        while index>=0:
            if s[index]==")":
                right+=1
            else:
                left+=1 
            if left==right:
                ans=max(ans,left*2)
            elif left>right:
                left=right=0
            index-=1 
        return ans 
    def longestValidParentheses(self, s: str) -> int:
        ans=0
        indexStack=[-1]
        for index,alphbet in enumerate(s):
            if alphbet=="(":
                indexStack.append(index)
            else:
                indexStack.pop()
                if not indexStack:
                    indexStack.append(index)
                else:
                    ans=max(ans,index-indexStack[-1])
        return ans 


            
        



def testCase0(instance:Solution=Solution()):
    assert instance.longestValidParentheses("(())")==4
    assert instance.longestValidParentheses(")")==0 
    assert instance.longestValidParentheses("(")==0 
    assert instance.longestValidParentheses("(()")==2
def wrongCase0(instance:Solution=Solution()):
    assert instance.longestValidParentheses(")(")==0
if __name__ =="__main__":
    testCase0()
    wrongCase0()

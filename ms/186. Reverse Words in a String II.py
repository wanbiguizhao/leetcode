from typing import List 
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        要提问的问题：s中每个单词被多少个空格区分。
        s中首尾是否包含额外的空格
        """
        def reversed(i,j):
            while i<j:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        leftIndex=0
        rightIndex=0
        constLen=len(s)
        while rightIndex<constLen:
            while rightIndex<constLen and  s[rightIndex]!=" ":
                rightIndex+=1
            reversed(leftIndex,rightIndex-1)
            while  rightIndex<constLen and s[rightIndex]==" ":
                rightIndex+=1
            leftIndex=rightIndex
        reversed(0,constLen-1)
def testCase0(instance:Solution=Solution()):
    # res=instance.reverseWords("    ")
    # print(res,res=="")
    # res=instance.reverseWords("    aaa   bb c")
    # print(res,res=="c bb aaa")
    input=list("abc ab c")
    instance.reverseWords(input)
    print(input)
    s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    instance.reverseWords(s)
    print(s)
if __name__ =="__main__":
    #testCase0()
    testCase0()


        
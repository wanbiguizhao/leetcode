


from typing import List 

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def nextParenthesis(left,right,oneRes):
            if right>left or left>n:
                return 
            if n==left and n == right:
                ansList.append(oneRes)
                return
             
            nextParenthesis(left+1,right,oneRes+"(")
            nextParenthesis(left,right+1,oneRes+")") 
        ansList=[] 
        nextParenthesis(0,0,"")
        return ansList

def testCase0(instance:Solution=Solution()):
    print(instance.generateParenthesis(3))
def wrongCase0(instance:Solution=Solution()):
    pass
if __name__ =="__main__":
    testCase0()
    wrongCase0()
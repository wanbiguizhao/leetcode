from typing import List
from unicodedata import digit 
class Solution:
    """_summary_
    
    """
    def letterCombinations(self, digits: str) -> List[str]:
        """
        排列加字典数据结构
        Runtime: 47 ms, faster than 42.87% of Python3 online submissions for Letter Combinations of a Phone Number.
        Memory Usage: 14 MB, less than 29.70% of Python3 online submissions for Letter Combinations of a Phone Number.

        Args:
            digits (str): _description_

        Returns:
            List[str]: _description_
        """
        def dsp(prefix,ith):
            if ith==len(digits):
                ans.append(prefix)
                return 
            for letter in mappingDigitToLetter[digits[ith]]:
                dsp(prefix+letter,ith+1)
        mappingDigitToLetter={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        if digits=="":
            return []
        ans=[]
        dsp("",0)
        return ans 
def testCase0(instance=Solution()):
    res=instance.letterCombinations("")
    print(res==[])
    res=instance.letterCombinations("7")
    print(res==["p","q","r","s"])
    res=instance.letterCombinations("77")
    print(res)
    res=instance.letterCombinations("798")
    print(len(res)==4*3*4)

if __name__ =="__main__":
    #testCase0()
    #testCase0()
    testCase0()
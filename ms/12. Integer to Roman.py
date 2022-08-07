from typing import List 

class Solution:
    def intToRoman(self, num: int) -> str:
        ans=""
        while num>1000:
            num-=1000
            ans+="M"
        if num>=900:
            num-=900
            ans+="CM"
        if num>=500:
            num-=500
            ans+="D"
        if num>=400:
            num-=400
            ans+="CD"
        while num>=100:
            num-=100
            ans+="C"
        if num>=90:
            num-=90
            ans+="XC"
        if num>=50:
            num-=50
            ans+="L"
        if num>=40:
            num-=40
            ans+="XL"
        while num>=10:
            num-=10
            ans+="X"
        ansCache={
            9:"IX",
            8:"VIII",
            7:"VII",
            6:"VI",
            5:"V",
            4:"IV",
            3:"III",
            2:"II",
            1:"I",
            0:""
        }
        return ans+ansCache[num]




def testCase0(instance:Solution=Solution()):
    print(instance.intToRoman(1))
    print(instance.intToRoman(29))
    print(instance.intToRoman(929))
    print(instance.intToRoman(9929))
    print(instance.intToRoman(920))
def wrongCase0(instance:Solution=Solution()):
    pass
if __name__ =="__main__":
    testCase0()
    wrongCase0()
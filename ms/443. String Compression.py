from csv import writer
from multiprocessing.context import assert_spawning
from turtle import write_docstringdict
from typing import List 

class Solution:
    def compress(self, chars: List[str]) -> int:
        def writeWords(begindex,word):
            for letter in word:
                chars[begindex]=letter
                begindex+=1 
        
        constLenChars=len(chars)
        if constLenChars==1:
            return 1
        writeIndex=0
        index=1
        count=1
        ans=0
        while index<constLenChars:
            if chars[index]==chars[index-1]:
                count+=1
            else:
                
                ans+=1
                writestr=chars[index-1]
                if count>1:
                    ans+=len(str(count))
                    writestr="{}{}".format(chars[index-1],count)
                writeWords(writeIndex,writestr)
                writeIndex+=len(writestr)
                count=1
            index+=1
        ans+=1
        writestr=chars[index-1]
        if count>1:
            ans+=len(str(count))
            writestr="{}{}".format(chars[index-1],count)
        writeWords(writeIndex,writestr)
        return ans 

def testCase0(instance:Solution=Solution()):
    assert instance.compress(chars = ["a","a","b","b","c","c","c"])== 6#["a","2","b","2","c","3"]
    assert instance.compress(chars = ["a","b","b","c","c","c"])==5# ["a","b","2","c","3"]
    assert instance.compress(chars = ["a","b","b","c"])== 4#["a","b","2","c"]
    assert instance.compress(chars = ["b","b","b"])== 2#["b","3"]
    print(instance.compress(chars = ["a","a","c","c","b","b","b"]))

def wrongCase0(instance:Solution=Solution()):
    pass
if __name__ =="__main__":
    testCase0()
    wrongCase0()
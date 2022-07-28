from telnetlib import WILL
from typing import List 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Q: 
        # 1. what the length of word in strs list
        # OK : the upper time complexity is 10*log(10) when program execute sort for one word
        # 2.  
        cache={}
        for word in strs:
            sortWord=str(sorted(word))# pay attention sort function will change the data type of str  , witch change from str to list . 
            if sortWord not in cache:
                cache[sortWord]=[]
            cache[sortWord].append(word)
        return list(cache.values())

def testCase0(instance:Solution=Solution()):
    res=instance.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(res,[["bat"],["nat","tan"],["ate","eat","tea"]])
    res=instance.groupAnagrams(["ab","bc"])
    print(res)
    res=instance.groupAnagrams([""])
    print(res)



if __name__ =="__main__":
    
    testCase0()
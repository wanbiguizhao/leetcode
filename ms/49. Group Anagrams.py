from collections import Counter
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
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 使用计数法,比较差。
        cache={}
        for word in strs:
            wordconvert=[0]*26
            for letter in word:
                wordconvert[ord(letter)-ord('a')]+=1
            strWordConvert="".join(map(lambda x: "{0:04}".format(x),wordconvert))
            if strWordConvert not in cache:
                cache[strWordConvert]=[]
            cache[strWordConvert].append(word)
        return list(cache.values())
def testCase0(instance:Solution=Solution()):
    res=instance.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(res,[["bat"],["nat","tan"],["ate","eat","tea"]])
    res=instance.groupAnagrams(["ab","bc"])
    print(res)
    res=instance.groupAnagrams([""])
    print(res)
def wrongCase0(instance:Solution=Solution()):
    # 没有注意到当一个字母重复十次以上时，计数法可能会有问题。
    # 错误的原因没有注意:  0 <= strs[i].length <= 100
    res=instance.groupAnagrams(["bdddddddddd","bbbbbbbbbbc"])
    print(res,len(res))


if __name__ =="__main__":
    
    testCase0()
    wrongCase0()
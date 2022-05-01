import imp
from typing import  List
from collections import defaultdict
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispalidrome(beg,end):

            while beg<=end:
                if s[beg]!=s[end]:
                    return False 
                beg+=1
                end-=1
            return True 
        # s[i,j] 是否是回文。
        # s[0,j] 中包含的回文类型
        #palindrome_cache={} # s[i,j] 是否是回文
        pre_ans_cache={} # s[0,k]包含的所有的回文结果
        pre_ans_cache[-1]=[[]]
        # 自底向上构建
        for index,x in enumerate(s):
            last_element_index=index
            pre_ans_cache[index]=[]

            while last_element_index>=0:
                if ispalidrome(last_element_index,index):
                    for pre_ans in pre_ans_cache[last_element_index-1]:
                        new_ans=pre_ans+[str(s[last_element_index:index+1])]
                        pre_ans_cache[index].append(
                            new_ans
                        )

                last_element_index-=1
        print(pre_ans_cache[len(s)-1])
        return pre_ans_cache[len(s)-1]
if __name__ == "__main__":
    instance=Solution()
    instance.partition("aab")
    instance.partition("aabbabbaa")
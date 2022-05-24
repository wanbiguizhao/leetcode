from typing import List 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # 速度更快
        def findWordBreak(si:int,pre_ans_str):
            if si==const_len:
                ans_list.append(pre_ans_str[:-1])
                return
            else:
                for word in wordSet:
                    # if visited[index]:
                    #     continue 
                    word_len=len(word)
                    if s[si:si+word_len]==word:
                        #visited[index]=True
                        findWordBreak(si+word_len,pre_ans_str+"{} ".format(word))
                        #visited[index]=False
        ans_list=[] 
        const_len=len(s)
        wordSet=set(wordDict)
        #visited=[False]*len(wordDict) # 只让使用一次时启用
        findWordBreak(0,"")
        #print(ans_list)
        return ans_list
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Runtime: 64 ms, faster than 22.31% of Python3 online submissions for Word Break II.

        def findWordBreak(si:int,pre_ans_list):
            if si==const_len:
                ans_list.append(" ".join([wordDict[x] for x  in pre_ans_list]))
                return
            else:
                for index,word in enumerate(wordDict):
                    # if visited[index]:
                    #     continue 
                    word_len=len(word)
                    if s[si:si+word_len]==word:
                        #visited[index]=True
                        findWordBreak(si+word_len,pre_ans_list+[index])
                        #visited[index]=False
        ans_list=[] 
        const_len=len(s)
        #visited=[False]*len(wordDict) # 只让使用一次时启用
        findWordBreak(0,[])
        #print(ans_list)
        return ans_list

if __name__ == "__main__":
    instance=Solution()
    #instance.wordBreak(s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"])
    instance.wordBreak("pineapplepenapple",["apple","pen","applepen","pine","pineapple"])


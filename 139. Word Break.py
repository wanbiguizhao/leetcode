from typing import  List
from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def judge_str(beg_index):
            if beg_index>=const_len:
                return True 
            for word in  word_first_alphabet_dict[s[beg_index]]:
                word_len=len(word)
                if const_len - beg_index>=word_len and s[beg_index:beg_index+word_len]==word:
                    if judge_str(beg_index+word_len):
                        return True 
            return False
        const_len=len(s)
        word_first_alphabet_dict=defaultdict(list)
        for word in wordDict:
            word_first_alphabet_dict[word[0]].append(word)
        ans=judge_str(0)
        return ans 
if __name__ == "__main__":
    instance=Solution()
    instance.wordBreak(s = "applepenapple", wordDict = ["apple","pen"])
    instance.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"])
    instance.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat","og"])
from curses import erasechar
from typing import List 
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 
        const_word_len=len(beginWord)
        beg_set=set([beginWord])
        end_set=set([endWord])
        wordSet=set(wordList)
        step=0
        while beg_set and end_set :
            step+=1
            tmp_set=set()
            for word in beg_set:
                for i in range(const_word_len):
                    for x in range(26):
                        change_word=word[:i]+chr(ord('a')+x)+word[i+1:]
                        if change_word in end_set:
                            return step+1
                        if change_word not in wordSet:
                            continue 
                        wordSet.remove(change_word)# 这一步要想清楚为什么？
                        tmp_set.add(change_word)
            beg_set=tmp_set
        if len(beg_set)>len(end_set):
            beg_set,end_set=end_set,beg_set
        return 0        

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 
        const_word_len=len(beginWord)
        beg_set=set([beginWord])
        end_set=set([endWord])
        wordSet=set(wordList)
        step=0
        while beg_set and end_set :
            step+=1
            tmp_set=set()
            for word in beg_set:
                for i in range(const_word_len):
                    for x in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                        change_word=word[:i]+x+word[i+1:]
                        if change_word in end_set:
                            return step+1
                        if change_word not in wordSet:
                            continue 
                        wordSet.remove(change_word)# 这一步要想清楚为什么？
                        tmp_set.add(change_word)
            beg_set=tmp_set
        if len(beg_set)>len(end_set):
            beg_set,end_set=end_set,beg_set
        return 0
# You are given an array of strings words. Each element of words consists of two lowercase English letters.

# Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

# Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

# A palindrome is a string that reads the same forward and backward.
from collections import Counter
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_counter=Counter(words)
        ans=0
        mid=0
        for word in word_counter.keys():
            reverse_word=word[1]+word[0]
            if word == reverse_word:
                if word_counter[word]%2==1:
                    mid=1
                ans+=4*( word_counter[word]//2)
            else:
                if word>reverse_word:
                    ans+=4*min(word_counter[word],word_counter[reverse_word])
        ans+=mid*2 # 这个非常重要
        return ans

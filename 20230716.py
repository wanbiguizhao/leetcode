# 阅读以下描述，写出可运行代码或者算法（算法需要给出算法的时间和空间复杂度），
# 代码/算法时间复杂度需小于n2  (n为字符串长度)，代码需要验证边界用例（s长度为5和50000）。
# Given a string s, partition s such that every substring of the partition is a palindrome （回文，即倒过来看与原字符串相同）.
# Return the minimum cuts needed for a palindrome partitioning of s.

# Example 1:  Input: s = "aabcc"    Output: 2   Explanation: partition ["aa","b","cc"] could be produced using 2 cuts.
# Example 2:  Input: s = "aaaaa"    Output: 0   Explanation: partition ["aaaaa"] is a palindrome, so no cut needed.

# Constraints:  
# 5 <= n <= 50000
# s consists of lower-case English letters (a-z) only. 

def max_palindrome(target_string,i,j):
    if len(target_string)==1:
        return 1
    l,r=0,len(target_string)-1
    while i>=l and j<=r:
        if target_string[i]==target_string[j]:
            i-=1
            j+=1
        else:
            break
    return i+1,j-1

def get_ans(s):
    # 找到某个单词的回文数据
    print(s)
    ans_l=0
    ans_r=0
    if not s:
        return 0 
    for i in range(len(s)-1):
        l1,r1=max_palindrome(s,i,i)
        l2,r2=max_palindrome(s,i,i+1)
        if r1-l1>r2-l2:
            if r1-l1>ans_r-ans_l:
                ans_l,ans_r=l1,r1 
        else:
            if r2-l2>ans_r-ans_l:
                ans_l,ans_r=l2,r2
    if ans_l==0 and ans_r==len(s)-1:
        return 0
    elif ans_l==0:
        return 1+ get_ans(s[ans_r+1:])
    elif ans_r==len(s)-1:
        return 1+  get_ans(s[0:ans_l])
    return 2+get_ans(s[0:ans_l])+get_ans(s[ans_r+1:])

    """
阅读以下描述，写出可运行代码或者算法（算法需要给出算法的时间和空间复杂度），
代码/算法时间复杂度需小于n2  (n为字符串长度)，代码需要验证边界用例（s长度为5和50000）。
Given a string s, partition s such that every substring of the partition is a palindrome （回文，即倒过来看与原字符串相同）.
Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:  Input: s = "aabcc"    Output: 2   Explanation: partition ["aa","b","cc"] could be produced using 2 cuts.
Example 2:  Input: s = "aaaaa"    Output: 0   Explanation: partition ["aaaaa"] is a palindrome, so no cut needed.

Constraints:  
5 <= n <= 50000
s consists of lower-case English letters (a-z) only. 

    """
# test case aaa 
# print(get_ans("aaa"),0)
# print(get_ans("aabcc"),2)
# print(get_ans("aabbbbbbcc"),2)
print(get_ans("aab"),2)



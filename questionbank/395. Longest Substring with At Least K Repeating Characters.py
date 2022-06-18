from collections import Counter 
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # pass 
        # 先找到肯定不能满足大于k的字符串。
        if len(s)<k:
            return 0 
        alphabet_count=Counter(s)
        if max(alphabet_count.values())<k:
            return 0 # 避免无效的查询
        ans=0
        beg_index=0
        for index,chr in enumerate(s):
            if alphabet_count[chr]<k:
                ans=max(ans,self.longestSubstring(s[beg_index:index],k))
                beg_index=index+1
        
        if beg_index==0:
            return len(s) # 可能存在整个字符串都是满足条件的情况。
        return max(ans,self.longestSubstring(s[beg_index:],k) ) # 避免死循环。

if __name__ == "__main__":
    instance=Solution()
    # instance.longestSubstring(s = "ababbc", k = 2)
    # instance.longestSubstring(s = "aaabb", k = 3)
    print(instance.longestSubstring(s = "bbaaacbd", k = 3))
    print(instance.longestSubstring(s = "bbaaabaaaa", k = 3))

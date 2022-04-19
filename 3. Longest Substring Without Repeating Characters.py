from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        left_index=0
        right_index=0
        alphabet_index={}
        while right_index<len(s):
            if s[right_index] in alphabet_index.keys():
                origin_index=alphabet_index[s[right_index]]
                for del_index in range(left_index,origin_index+1):
                    del alphabet_index[s[del_index]] # 删除重复区间的字符串。
                left_index=origin_index+1 # 记录新的位置
            else:
                ans=max(right_index-left_index+1,ans)
            alphabet_index[s[right_index]]=right_index
            right_index+=1
        return ans 

if __name__=="__main__":
    instance=Solution()
    instance.lengthOfLongestSubstring("a")
    instance.lengthOfLongestSubstring("aa")
    instance.lengthOfLongestSubstring("abcdc")
    instance.lengthOfLongestSubstring("abcdff")
                

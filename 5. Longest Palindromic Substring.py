class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 马拉车算法似乎忘了。
        if len(s)==1:
            return s 
        ans=""
        const_s_len=len(s)
        for index in range(2*const_s_len):
            left_index=index//2
            right_index=(index+1)//2
            while left_index>=0 and right_index< const_s_len and s[left_index]==s[right_index]:
                if right_index-left_index+1 >len(ans):
                    ans=s[left_index:right_index+1]
                left_index-=1
                right_index+=1
        return "".join(ans)

if __name__=="__main__":
    instance=Solution()
    ans=instance.longestPalindrome(s = "cbbd")
    ans=instance.longestPalindrome(s = "bbabd")
    ans=instance.longestPalindrome(s = "bbabb")



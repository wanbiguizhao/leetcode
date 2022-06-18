from turtle import right 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 中心距离算法
        if len(s)==1:
            return s 
        ans=""
        const_s_len=len(s)
        for index in range(2*const_s_len):
            left_index=index//2 # 核心
            right_index=(index+1)//2 # 核心 对于bab left_index == right_index left_index+1=right_index 两种可能
            while left_index>=0 and right_index< const_s_len and s[left_index]==s[right_index]:
                if right_index-left_index+1 >len(ans):
                    ans=s[left_index:right_index+1]
                left_index-=1
                right_index+=1
        return "".join(ans)
    def longestPalindrome(self, s: str) -> str:
        # 马拉车算法  manacher 算法
        # https://www.youtube.com/watch?v=5Rqomc7na7A
         
        if len(s)==1:
            return s 
        max_right_index=0
        center_index=0
        auxiliary_s="#"+"#".join(s)+"#"
        best_start=0
        dp=[0]*len(auxiliary_s)
        for index,alphabet in enumerate(auxiliary_s):
            mirror_index=2*center_index-index
            r=0
            if  max_right_index>index:
                mirror_index=2*center_index-index
                if mirror_index>0:
                    r=dp[mirror_index]
                r=min(r,max_right_index-index)
            # 搜索一下
            left_index=index-r
            right_index=index+r
            while left_index>=0 and right_index< len(auxiliary_s) and auxiliary_s[left_index]==auxiliary_s[right_index]:
                left_index-=1
                right_index+=1
            dp[index]=(-left_index+right_index)//2-1
            r=dp[index]
            if index+r>max_right_index:
                center_index=index
                max_right_index=index+r
        maxLen, centerIndex = max((n, i) for i, n in enumerate(dp))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]

if __name__=="__main__":
    instance=Solution()
    # ans=instance.longestPalindrome(s = "cbbd")
    # print(ans)
    # ans=instance.longestPalindrome(s = "bbabd")
    # print(ans)
    # ans=instance.longestPalindrome(s = "bbabb")
    # print(ans)

    ans=instance.longestPalindrome(s = "aacabdkacaa")



class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s=list(s)
        S_LEN=len(s)
        ans=0
        for index in range(S_LEN//2):
            p_index=S_LEN-index-1 #回文的索引
            while(s[index]!=s[p_index]): 
                p_index-=1
            if index!=p_index:
                ans+=S_LEN-index-1-p_index
                s[S_LEN-index-1],s[p_index]=s[p_index],s[S_LEN-index-1]
            else:
                ans+=S_LEN//2-index
            

        return ans  

if __name__=="__main__":
    solution=Solution() 
    ans=solution.minMovesToMakePalindrome("aabbc")
    print(ans)
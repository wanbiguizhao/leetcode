
class Solution:
    def minMovesToMakePalindrome_1(self, s: str) -> int:
        s=list(s)
        S_LEN=len(s)
        ans=0
        count=0
        for index in range(S_LEN//2):
            p_index=S_LEN-count-1 #回文的索引
            while(s[index]!=s[p_index]): 
                p_index-=1
            if index!=p_index:
                rest_move=S_LEN-count-1-p_index
                ans+=rest_move
                while rest_move:
                    s[p_index],s[p_index+1]=s[p_index+1],s[index]
                    rest_move-=1
                    count+=1
            else:
                ans+=S_LEN//2-index
            

        return ans  
    def minMovesToMakePalindrome(self, s: str) -> int:
        #使用堆栈的思想
        s=list(s)
        ans=0
        while s:
            for i in range(len(s)):
                if s[i]==s[-1]:
                    if i==len(s)-1:
                        s.pop(-1)
                        ans+=len(s)//2 
                    else:
                        ans+=i
                        s.pop(-1)
                        s.pop(i)
                    break 
            

        return ans 
if __name__=="__main__":
    solution=Solution() 
    ans=solution.minMovesToMakePalindrome("aabbc")
    print(ans)
    ans=solution.minMovesToMakePalindrome("caabb")
    print(ans)
    ans=solution.minMovesToMakePalindrome("c")
    print(ans)
    ans=solution.minMovesToMakePalindrome("cc")
    print(ans)
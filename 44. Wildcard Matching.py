class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 递归  p[0]==*
        # 递归  p[0]==?
        #       p[0]字符串。 
        if not s and not p:
            return True 
        if p and not s:
            if p[0]=="*":
                return True
            else:
                return False 
        if s and not p:
            return False 
        # p和s 都不为空。
        if p[0]=="*":
            if self.isMatch(s[1:],p[1:]):
                return True 
            elif self.isMatch(s,p[1:]):
                return True 
            else: 
                return self.isMatch(s[1:],p)
        elif p[0]=="?":
            return self.isMatch(s[1:],p[1:])
        elif s[0]==p[0]:
            return self.isMatch(s[1:],p[1:])
        else:
            return False


if __name__ == "__main__":
    instance=Solution()
    print(instance.isMatch(s = "aa", p = "a")==False)
    print(instance.isMatch(s = "aa", p = "aa*")==True)
    print(instance.isMatch( s = "cb", p = "?a")==False)

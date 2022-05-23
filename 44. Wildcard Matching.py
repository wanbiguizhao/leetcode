


import re


class Solution:
    
    def isMatch(self, s: str, p: str) -> bool:
        # 递归  p[0]==*
        # 递归  p[0]==?
        #       p[0]字符串。 
        # 对p进行初始化处理，替换到多余的*
        def doMatch(s:str,p:str):
            if  s and  p:
                i=0
                while  s[i]==p[i]:
                    i=i+1
                    if i==len(p) or i ==len(s):
                        return doMatch(s[i:],p[i:])
                if p[i]=="*":
                    if doMatch(s[i:],p[i+1:]):
                        return True 
                    elif doMatch(s[i+1:],p[i+1:]):
                        return True 
                    elif doMatch(s[i+1:],p[i:]):
                        return True 
                    return False 
                if p[i]=="?":
                    return doMatch(s[i+1:],p[i+1:])
                return False 
            elif  s and not p:
                return False 
            elif p and not s:
                if p[0]=="*":
                    return doMatch(s,p[1:])
                return False
            else:
                return True  

        new_p="^"
        for x in p:
            if new_p[-1]=="*" and x=="*":
                continue 
            else:
                new_p+=x
        # 需要进行一些减枝条算法
        i=0
        p=new_p[1:]
        while  p[i]!="*" or p[i]!="?":
            if p[i]!=s[i]:
                return False
            i=i+1
            if i ==len(s)or i==len(p):
                break 
        i=-1
        while  p[i]!="*" or p[i]!="?":
            if p[i]!=s[i]:
                return False
            i=i-1
            if i+len(s)==0 or i+len(p)==0:
                break 
        #p=new_p[1:]
        return doMatch(s,new_p[1:])


if __name__ == "__main__":
    instance=Solution()
    # print(instance.isMatch(s = "aa", p = "a")==False)
    # print(instance.isMatch(s = "aa", p = "aa*")==True)
    # print(instance.isMatch( s = "cb", p = "?a")==False)
    # print(instance.isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab","***bba**a*bbba**aab**b"))
    #instance.isMatch("bbbbbbbabbaabbabbbbaaabbabbabaaabbababbbabbbabaaabaab","b*b*ab**ba*b**b***bba")
    #instance.isMatch("adceb","*a*b")
    instance.isMatch("aa","*")
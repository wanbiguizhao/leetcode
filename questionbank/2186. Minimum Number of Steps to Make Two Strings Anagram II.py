from collections import Counter

class Solution:
    # 空间换时间
    # counter 
    def minSteps(self, s: str, t: str) -> int:
        s_counter=Counter(s)
        t_counter=Counter(t)
        ans=0
        alphabet_set=set()
        alphabet_set.update(s)
        alphabet_set.update(t)
        for alphabet in alphabet_set:
            ans+=abs(s_counter[alphabet]-t_counter[alphabet])
        return ans 
if __name__=="__main__":
    solution=Solution()
    ans=solution.minSteps("abc","cba")
    print(ans)
    ans=solution.minSteps("ac","cba")
    print(ans)
    ans=solution.minSteps("abc","def")
    print(ans)
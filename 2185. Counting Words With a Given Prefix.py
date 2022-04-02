from typing import List 
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans=0
        for word in words:
            # 边界值非常重要            if len(word)>=len(pref) and word[:len(pref)] == pref:
                ans+=1
        return ans


if __name__=="__main__":
    solution=Solution()
    ans=solution.prefixCount(["a","b","bc"],"b")
    print(ans)
    ans=solution.prefixCount(["a","b","bc","bba"],"bba")
    print(ans)
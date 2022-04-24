from typing import List 
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def _generate(left_cnt,right_cnt,pre_str):
            if right_cnt==n:
                ans.append(pre_str) 
                return 
            if left_cnt<n:
                _generate(left_cnt+1,right_cnt,pre_str+"(")
            if right_cnt<left_cnt:
                _generate(left_cnt,right_cnt+1,pre_str+")")
            
        ans=[]
        _generate(0,0,"")
        return ans 
if __name__ == "__main__":
    instance = Solution()
    print(instance.generateParenthesis(3))
        
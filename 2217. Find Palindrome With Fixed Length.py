import pysnooper
from typing import List
from copy import copy


class Solution:
    # 回文问题转化为长度对称问题
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        ans_list=[]
        if intLength%2==0:
            # 偶数
            half_length= intLength//2
            base=10**(half_length-1)
            #ans_list=[ base+query-1 for query in queries]
            mid_ans_list= [ base+query-1 for query in queries]
            for data in mid_ans_list:
                if data>base*10-1:
                    ans_list.append(-1)
                else:
                    ans_list.append(int(str(data)+str(data)[::-1]))
        else:
            half_length= intLength//2+1
            base=10**(half_length-1) 
            mid_ans_list= [ base+query-1 for query in queries]
            for data in mid_ans_list:
                if data>base*10-1:
                    ans_list.append(-1)
                else:
                    ans_list.append(int(str(data)+str(data)[::-1][1:]))
        return ans_list

if __name__=="__main__":
    instance=Solution()
    ans=instance.kthPalindrome([2,4,6],4)
    print(ans)
    ans=instance.kthPalindrome([2,4,100],3)
    print(ans)


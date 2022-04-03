from codecs import xmlcharrefreplace_errors
import heapq


import heapq
from collections import Counter
from os import stat_result
from tkinter.tix import Tree

from cv2 import repeat
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ORDER_INDEX=0
        CHAR_INDEX=1
        REMAING_INDEX=2
        ans=[]
        repeat_count=0
        status_register=[ [-ord(xchr), xchr , num ] for xchr ,num in Counter(s).items()]
        heapq.heapify(status_register)
        while status_register:
            one_status=heapq.heappop(status_register) # order, 
            if not ans :
                ans.append( one_status[CHAR_INDEX])
                one_status[REMAING_INDEX]-=1
                repeat_count=1
            else:
                if ans[-1] == one_status[CHAR_INDEX] and repeat_count == repeatLimit:
                    # 使用下一个的情况
                    if not status_register:
                        break
                    little_one_status=heapq.heappop(status_register)
                    ans.append(little_one_status[CHAR_INDEX])
                    little_one_status[REMAING_INDEX]-=1
                    if little_one_status[REMAING_INDEX]>0:
                        heapq.heappush(status_register,little_one_status)

                else: 
                    if ans[-1]!= one_status[CHAR_INDEX] :
                        repeat_count=0 
                    repeat_count+=1
                    ans.append( one_status[CHAR_INDEX])
                    one_status[REMAING_INDEX]-=1                    
            if one_status[REMAING_INDEX]>0:
                heapq.heappush(status_register,one_status)
        return "".join(ans)


if __name__=="__main__":
    solution=Solution()
    # ans=solution.repeatLimitedString("aabbcc",repeatLimit=2)
    # print(ans)
    # ans=solution.repeatLimitedString("abc",repeatLimit=1)
    # print(ans)
    ans=solution.repeatLimitedString("aaaaabbbbcccc",repeatLimit=1)
    print(ans)
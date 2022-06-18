import heapq
from collections import Counter
from inspect import stack
from urllib.parse import scheme_chars

class Solution:
    def repeatLimitedString_heaqpq(self, s: str, repeatLimit: int) -> str:
        # heapq
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
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # alphabet
        s_counter=Counter(s)
        status_stack=[]
        for x in range(ord('a'),ord('z')+1):
            xchar=chr(x)
            if xchar in s_counter:
                status_stack.append([ 
                    xchar,
                    s_counter[xchar] 
                ])
                # 按照z->a 的顺序,存储位置
        ans=""
        while len(status_stack)>=2:
            top_chr, top_count =status_stack[-1]
            sec_chr, sec_count = status_stack[-2]
            if top_count>repeatLimit:
                ans+=top_chr*repeatLimit
                status_stack[-1][1]-=repeatLimit
                ans+=sec_chr
                sec_count-=1
                if sec_count>0:
                    status_stack[-2][1]=sec_count 
                else:
                    status_stack.pop(-2)
            else:
                ans+=top_chr*top_count
                status_stack.pop(-1)
        if not ans or (len(status_stack)==1 and ans[-1] != status_stack[0][0]):
            ans+=min(repeatLimit,status_stack[0][1])*status_stack[0][0]
        return ans 




if __name__=="__main__":
    solution=Solution()
    # ans=solution.repeatLimitedString("aabbcc",repeatLimit=2)
    # print(ans)
    # ans=solution.repeatLimitedString("abc",repeatLimit=1)
    # print(ans)
    ans=solution.repeatLimitedString("aaaaabbbbcccc",repeatLimit=1)
    print(ans)
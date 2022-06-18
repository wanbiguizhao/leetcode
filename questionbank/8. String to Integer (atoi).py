from doctest import FAIL_FAST


class Solution:
    def myAtoi(self, s: str) -> int:
        # 状态机进行识别。
        max_num=2**31-1
        min_num=-2**31
        #s=s.replace(" ","") # 替换空格
        beg_index=-1
        end_index=-1
        state_A=True # beg ,get letter, white space 
        state_B=False # 状态B的情况，
        state_C=False
        for index,x in enumerate(s):
            if state_A:
                if x =="+" or x  =="-":
                    state_A=False
                    state_B=True
                    beg_index=index
                elif x.isdigit():
                    state_A=False
                    state_C=True
                    beg_index=index
                    end_index=index
                elif x ==" ":
                    state_A=True 
                else:
                    break 
            elif state_B:
                if x.isdigit():
                    state_B=False
                    state_C=True 
                    end_index=index
                else:
                    break
            elif state_C:
                if x.isdigit():
                    end_index=index
                else:
                    break
        
        ans=0
        if not state_C:
            return ans 
        add_flag= -1 if s[beg_index]=='-' else 1  
        if s[beg_index] =="+" or s[beg_index]  =="-":
            beg_index+=1
        while beg_index<=end_index:
            ans= ans*10 + add_flag*int(s[beg_index])
            beg_index+=1
            if ans > max_num :
                return max_num
            elif ans < min_num:
                return min_num
        return ans 

if __name__ == "__main__":
    instance = Solution()
    # print(instance.myAtoi("---111"),-111)
    # print(instance.myAtoi("-+12"),12)
    # print(instance.myAtoi("-+12--"),12)
    # print(instance.myAtoi("-+000120--"),120)
    print(instance.myAtoi("-00012   0--"),-12)
    print(instance.myAtoi("-00  012   0--"),0)
    print(instance.myAtoi("00012   0--"),12)
    print(instance.myAtoi("words and 987"))
    print(instance.myAtoi("words and 9"))

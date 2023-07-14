from typing import List
from collections import Counter,defaultdict
import functools
class Solution:
    # tag: 滑动窗口, 窗口里面的数据是可以做任意调整的，调整的数据就是需要是可以让窗口外的数据达到平衡
    # 窗口外的字母需要达到平衡所确实的字母数，窗口内能否提供，如果可以提供，那么记录窗口的值。
    def run(self,wasd_string ) -> int:
        wasd_counter=Counter(wasd_string)
        if wasd_counter["W"]==wasd_counter["A"] and wasd_counter["W"]==wasd_counter["S"] and wasd_counter["W"]==wasd_counter["D"]:
            return 0
        ans=len(wasd_string)
        left=0
        right=0# 闭区间
        windows_length=0
        free_char_num=0
        wasd_counter[wasd_string[0]]-=1# 这个字符敲掉了
        # 是一个滑动窗口，窗口内的所有字符，可以完成把不平衡的字符串替换的平衡，那么就没有任何问题。
        while right<len(wasd_string):
            max_char_count=max(wasd_counter.values())
            windows_length=right-left+1
            free_char_num=windows_length-(max(wasd_counter.values())*4-sum(wasd_counter.values()))# 如果让窗口中所有的元素进行替换操作
            # 看一下是否还剩余元素
            if free_char_num>=0 and free_char_num%4==0:
                if windows_length<ans:
                    ans=windows_length
                    #print(wasd_string[left:right+1])
                wasd_counter[wasd_string[left]]+=1
                left+=1
            else:
                right+=1
                if right< len(wasd_string):
                    wasd_counter[wasd_string[right]]-=1
        return ans
            
s=Solution()
print(
    s.run("WASD")
)
print(
    s.run("WASDDDDD")
)
print(
    s.run("WASDWAAD")
)

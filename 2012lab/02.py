
from typing import List
from collections import Counter,defaultdict
import functools
class Solution:
    # tag: 排序
    def run(self, string_list: List[str]) -> str:
        string_list=[sorted(word) for word in string_list]# bug fix : but ubt btu 可能出现割裂，先word排序，然后再统计
        string_counter=Counter(string_list)
        sort_list=[]
        for word,cnt in string_counter.items():
            # 构建一个sort排序序列
            sort_list.append(
                [-cnt,
                len(word),
                "".join(sorted(word))]
            )
        sort_list=sorted(sort_list)
        ans=[]
        for pairs in sort_list:
            ans.extend([pairs[2]]*(-pairs[0]))
        return " ".join(ans)
    def run(self, string_list: List[str]) -> str:
        #节省存储空间
        def comp(a:List,b:List):
            if a[0]>b[0]:
                return -1
            elif a[0]<b[0]:
                return 1 
            else:
                if len(a[1])==len(b[1]):
                    if a[1]>b[1]:
                        return 1
                    else:
                        return -1
                elif len(a[1])>len(b[1]):
                    return 1 
                else:
                    return -1
            
        string_list=["".join(sorted(word)) for word in string_list]
        string_counter=Counter(string_list)
        sort_list=sorted([ (b,a) for a,b in string_counter.items()],key=functools.cmp_to_key(comp))
        ans=[]
        for pairs in sort_list:
            ans.extend([pairs[1]]*(pairs[0]))
        return " ".join(ans)
s=Solution()
print(s.run(
    ["this","is","apple"]
))
print(s.run(
    ["this","is","an","apple"]
))
print(s.run(
    ["This","is","an","apple"]
)) 
print(s.run(
    ["This","is","is","in","my","sister","in","the","house"]
))
print(s.run(
    ["abc","bca","ddd","ded","my","sister","in","the","house"]
))
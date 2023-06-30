
from typing import List
from collections import Counter,defaultdict
class Solution:
    def run(self, string_list: List[str]) -> str:
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
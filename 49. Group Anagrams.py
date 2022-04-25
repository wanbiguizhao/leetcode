from typing import List 
from collections import Counter,defaultdict
class Solution:
    def groupAnagrams_1(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        record_index_info=defaultdict(lambda:[])
        for one_str in strs:
            key_pre=""
            cnt=Counter(one_str)
            # 桶排序不行
            for x in['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                if cnt[x]!=0:
                    key_pre=key_pre+str(cnt[x])+ x
            record_index_info[key_pre].append(one_str)
        return [rec for rec in record_index_info.values() ]
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        record_index_info=defaultdict(lambda:[])
        for one_str in strs:
            key_pre="".join(sorted(one_str))
            record_index_info[key_pre].append(one_str)
        return [rec for rec in record_index_info.values() ]


if __name__ == "__main__":
    instance=Solution()
    print(instance.groupAnagrams(["","bbc","cbb","abc"]))
    print(instance.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
from typing import List 
from collections import Counter,defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        record_index_info=defaultdict(lambda:[])
        for one_str in strs:
            key_pre=""
            cnt=Counter(one_str)
            for x in range(ord('a'),ord('z')+1):
                key_pre=key_pre+str(cnt[chr(x)])+ chr(x) 
            record_index_info[key_pre].append(one_str)
        return [rec for rec in record_index_info.values() ]

if __name__ == "__main__":
    instance=Solution()
    print(instance.groupAnagrams(["","bbc","cbb","abc"]))
    print(instance.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
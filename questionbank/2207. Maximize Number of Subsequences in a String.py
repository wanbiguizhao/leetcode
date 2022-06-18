from typing import List 

class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        origin_pattern_count=0
        pattern_0_index_list=[]
        pattern_1_index_list=[]
        for index,alphbabet in enumerate(text):
            if alphbabet==pattern[0]:
                pattern_0_index_list.append(index)
            if alphbabet==pattern[1]:
                pattern_1_index_list.append(index)
        pattern_1_index=pattern_0_index=0
        while pattern_1_index<len(pattern_1_index_list) and pattern_0_index < len(pattern_0_index_list):
            if pattern_0_index_list[pattern_0_index]<pattern_1_index_list[pattern_1_index]:
                origin_pattern_count+=(len(pattern_1_index_list)-pattern_1_index)
                pattern_0_index+=1
            else:
                pattern_1_index+=1
        
            
        return max( len(pattern_0_index_list),len(pattern_1_index_list) )+origin_pattern_count
            
if __name__ == "__main__":
    instance = Solution()
    # instance.longestRepeating("babaccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"*200,"bcb",[1,3,3])
    ans=instance.maximumSubsequenceCount("abdcdbc","ac")      
    print(ans)
    ans=instance.maximumSubsequenceCount("vnedkpkkyxelxqptfwuzcjhqmwagvrglkeivowvbjdoyydnjrqrqejoyptzoklaxcjxbrrfmpdxckfjzahparhpanwqfjrpbslsyiwbldnpjqishlsuagevjmiyktgofvnyncizswldwnngnkifmaxbmospdeslxirofgqouaapfgltgqxdhurxljcepdpndqqgfwkfiqrwuwxfamciyweehktaegynfumwnhrgrhcluenpnoieqdivznrjljcotysnlylyswvdlkgsvrotavnkifwmnvgagjykxgwaimavqsxuitknmbxppgzfwtjdvegapcplreokicxcsbdrsyfpustpxxssnouifkypwqrywprjlyddrggkcglbgcrbihgpxxosmejchmzkydhquevpschkpyulqxgduqkqgwnsowxrmgqbmltrltzqmmpjilpfxocflpkwithsjlljxdygfvstvwqsyxlkknmgpppupgjvfgmxnwmvrfuwcrsadomyddazlonjyjdeswwznkaeaasyvurpgyvjsiltiykwquesfjmuswjlrphsdthmuqkrhynmqnfqdlwnwesdmiiqvcpingbcgcsvqmsmskesrajqwmgtdoktreqssutpudfykriqhblntfabspbeddpdkownehqszbmddizdgtqmobirwbopmoqzwydnpqnvkwadajbecmajilzkfwjnpfyamudpppuxhlcngkign"
,"rr")      
    print(ans)
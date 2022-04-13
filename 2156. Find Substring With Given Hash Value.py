class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        mapping_value={}
        for num_th in range(1,26+1):
            mapping_value[ chr( ord('a')+num_th-1 )]=num_th
        const_k=k
        
        first_sum_value=0
        index=0
        while index<const_k:
            first_sum_value=first_sum_value+ mapping_value[s[index]]*power**index
            index+=1 
        if first_sum_value%modulo==hashValue:
            return s[0:index]
        while index<len(s):
            first_sum_value=(first_sum_value - mapping_value[s[index-const_k]])//power + mapping_value[s[index] ]*power**(const_k-1)
            if first_sum_value%modulo==hashValue:
                return s[index-const_k+1 :index+1]
            index+=1

if __name__=="__main__":
    instance=Solution()
    print(instance.subStrHash( s = "leetcode", power = 7, modulo = 20, k = 2, hashValue = 0))
    print(instance.subStrHash(s = "fbxzaad", power = 31, modulo = 100, k = 3, hashValue = 32))
    print(instance.subStrHash( s = "laetcodee", power = 7, modulo = 20, k = 2, hashValue = 0))
        

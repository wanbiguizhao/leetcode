class Solution:
    def subStrHash_TLE(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        mapping_value={}
        for num_th in range(1,26+1):
            mapping_value[ chr( ord('a')+num_th-1 )]=num_th
        const_k=k
        const_power_k=power**(const_k-1)
        first_sum_value=0
        index=0
        while index<const_k:
            first_sum_value=first_sum_value+ mapping_value[s[index]]*power**index
            index+=1 
        if first_sum_value%modulo==hashValue:
            return s[0:index]
        while index<len(s):
            first_sum_value=(first_sum_value - mapping_value[s[index-const_k]])//power + mapping_value[s[index] ]*const_power_k
            if first_sum_value%modulo==hashValue:
                return s[index-const_k+1 :index+1]
            index+=1
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        
        def val(c):
            return ord(c)-ord('a')+1
        
        
        const_k=k
        const_max_power_k=(power**(const_k))%modulo
        hashed=0
        
        for index,ch in reversed(list(enumerate(s))):
            hashed=(hashed*power + val(ch))%modulo
            if index+const_k<len(s):
                hashed=(hashed - val(s[index+const_k])*const_max_power_k)%modulo
            if hashed == hashValue:
                best_left=index
        return s[best_left:best_left+const_k]

if __name__=="__main__":
    instance=Solution()
    print(instance.subStrHash( s = "leetcodee", power = 7, modulo = 20, k = 2, hashValue = 0))
    print(instance.subStrHash(s = "fbxzaad", power = 31, modulo = 100, k = 3, hashValue = 32))
    print(instance.subStrHash( s = "laetcodee", power = 7, modulo = 20, k = 2, hashValue = 0))
        

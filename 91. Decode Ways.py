class Solution:
    def numDecodings_1(self, s: str) -> int:
        def _numDecodings(s):
            if s in memory:
                return memory[s]
            if not s:
                memory[s]=1
                return memory[s] 
            if len(s)==1:
                if s[0] in mapping:
                    memory[s]=1
                    return memory[s] 
                else:
                    memory[s]=0
                    return memory[s]
            #len(s)>=2 
            s_1=0
            s_2=0
            if s[0] in mapping:
                s_1=_numDecodings(s[1:])
            if s[0]+s[1] in mapping:
                s_2=_numDecodings(s[2:])
            memory[s]=s_1+s_2
            return memory[s]
        if s[0]=='0':
            return 0
        memory={}
        mapping={} # mapping['A']='1' mapping['1']='A'
        for x in range(26):
            mapping[chr(x+ord('A'))]=str(x+1)
            mapping[str(x+1)]=chr(x+ord('A'))
        return _numDecodings(s)
    def numDecodings(self, s: str) -> int:
        def _numDecodings(s):
            if s in memory:
                return memory[s]
            if s[0]=="0":
                memory[s]=0
                return memory[s]
            if len(s)==1:
                memory[s]=0
                return memory[s]
            if len(s)==2:
                if int(s)%10==0:
                    memory[s]=0
                else:
                    memory[s]=1 # 这点十分重要，所有合法的len(s)==2 时，s 长度为2的都已经找到了。 00 01 -> 99 长度为2的只有11-19 21-26 其他的长度都为1 
                return memory[s]
            if 1<=int(s[:2]) and int(s[:2])<=26:
                memory[s] = _numDecodings(s[1:]) + _numDecodings(s[2:])
            else:
                memory[s] = _numDecodings(s[1:])
            return memory[s]
        memory={}
        for x in range(26):
            memory[str(x+1)]=len(str(x+1))
        memory['10']=1 # 已经把所有的合法数字组合找到。
        memory['20']=1 # 
        memory['']=0
        memory['0']=0
        return _numDecodings(s)
        
if __name__ == "__main__":
    instance=Solution()
    print(instance.numDecodings("06"),
    instance.numDecodings("1"),
    instance.numDecodings("12"),
    instance.numDecodings("1122"),
    instance.numDecodings("626"),
    instance.numDecodings("111111111111111111111111111111111111111111111"),
    instance.numDecodings_1("111111111111111111111111111111111111111111111"),
    instance.numDecodings_1("230"),
    instance.numDecodings("230")
    )
        
class Solution:
    def numDecodings(self, s: str) -> int:
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
        
if __name__ == "__main__":
    instance=Solution()
    print(instance.numDecodings("06"),
    instance.numDecodings("1"),
    instance.numDecodings("12"),
    instance.numDecodings("1122"),
    instance.numDecodings("626"),
    instance.numDecodings("111111111111111111111111111111111111111111111")
    )
        
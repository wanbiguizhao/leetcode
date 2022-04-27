class Solution:
    def numDecodings(self, s: str) -> int:
        def _numDecodings(s):
            if not s:
                return 1 
            s_1=0
            if len(s)==1:
                if s[0] in mapping:
                    return 1 
                else:
                    return 0 
            #len(s)>=2 
            s_1=0
            s_2=0
            if s[0] in mapping:
                s_1=_numDecodings(s[1:])
            if s[0]+s[1] in mapping:
                s_2=_numDecodings(s[2:])
            return s_1+s_2
        if s[0]==0:
            return 0
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
    instance.numDecodings("626")
    )
        
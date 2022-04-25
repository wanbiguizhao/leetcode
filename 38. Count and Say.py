from pickle import EMPTY_TUPLE


class Solution:
    def countAndSay(self, n: int) -> str :
        base_str="1"
        if n==1:
            return base_str
        for round in range(n-1):
            tmp_str=""
            count=1
            pre_alphabet=base_str[0]
            for i in range(1,len(base_str)):
                if base_str[i]==base_str[i-1]:
                   count+=1
                else:
                    tmp_str=tmp_str+str(count)+pre_alphabet
                    count=1
                    pre_alphabet=base_str[i]
            # 注意后续值的处理
            base_str=tmp_str+str(count)+pre_alphabet
        return base_str 
if __name__ == "__main__":
    instance=Solution()
    #instance.search([4,5,6,7,8,1,2,3],8)
    print(instance.countAndSay(1))
    print(instance.countAndSay(2))
                
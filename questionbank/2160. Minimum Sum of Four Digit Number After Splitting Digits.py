from collections import Counter
class Solution:
    def minimumSum2(self, num: int) -> int:
        # num-> abcd  假设 a>b>c>d 
        # 结果是， （a+b）*10 + c+d的情况，其实就是保证 a+b  最小，然后排序
        ans=0
        bulket=[0]*10
        while num>0:
            bulket[num%10]+=1
            num=num//10
        cnt=0
        for i in range(10):
            while bulket[i]>0:
                cnt+=1
                bulket[i]-=1
                if cnt<=2:
                    ans+= i*10
                    continue
                ans+= i
        return ans
    def minimumSum(self, num: int) -> int:
        ans=0
        str_num=sorted(str(num))
        num_counter=Counter(str_num)
        cnt=0
        for i in ["0","1","2","3","4","5","6","7","8","9"]:
            while num_counter[i]>0:
                cnt+=1
                num_counter[i]-=1
                if cnt<=2:
                    ans+= int(i)*10
                    continue
                ans+= int(i)
        return ans
                
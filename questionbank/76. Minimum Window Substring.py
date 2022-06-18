from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans_letter_counter=len(s)+1
        ans=""
        t_index=[]
        t_counter=Counter(t)
        for index,x in enumerate(s):
            if x in t_counter.keys():
                t_index.append(index)
        counter=Counter()
        queue_letter=[]        
        for index,s_index in enumerate(t_index):
            letter_x=s[s_index]
            counter[letter_x]+=1
            queue_letter.append([letter_x,s_index])
            while counter[queue_letter[0][0]]>t_counter[queue_letter[0][0]]:
                counter[queue_letter[0][0]]-=1
                queue_letter.pop(0)
            check_flag=True
            for x in t_counter.keys():
                if counter[x]<t_counter[x]:
                    check_flag=False 
                    break
            if check_flag and queue_letter[-1][1]-queue_letter[0][1]+1 <ans_letter_counter:
                ans=s[queue_letter[0][1]:queue_letter[-1][1]+1]
                ans_letter_counter=len(ans)
        #print(ans)
        return ans 

if __name__ == "__main__":
    instance=Solution()
    # instance.minWindow( s = "ADOBECODEBANC", t = "ABC")
    # instance.minWindow( s = "a", t = "a")
    # instance.minWindow( s = "a", t = "aa")
    #instance.minWindow( s = "aa", t = "aa")
    instance.minWindow( s = "cabwefgewcwaefgcf",t="cae")
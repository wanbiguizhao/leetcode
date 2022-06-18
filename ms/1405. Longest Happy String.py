import pip
from sklearn import pipeline


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        if a+b+c==0:
            return ""
        ans=""
        pipeline=[]
        if a!=0:
            pipeline.append([a,"a"])
        if b!=0:
            pipeline.append([b,"b"])
        if c!=0:
            pipeline.append([c,"c"]) 
        pipeline.sort()
        last_count=0
        while pipeline:
            cnt,letter=pipeline.pop()
            if ans and ans[-1]==letter and last_count==2:
                return ans 
            if cnt>=2 and  (not ans or ans[-1]!=letter ):
                ans=ans+letter+letter 
                cnt-=2
                last_count=2
            else:
                ans=ans+letter
                cnt-=1
                last_count=1
            if pipeline:
                cntx,lettery=pipeline.pop()
                ans=ans+lettery
                cntx-=1
                last_count=1
                if cntx>0:
                    pipeline.append([cntx,lettery])
            if cnt>0:
                pipeline.append([cnt,letter])

            pipeline.sort()
        return ans 

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # 使用堆排序
        # 然后一个字母一个字母的加。
        import heapq
        ans,maxheap="",[]
        for cnt,letter in [[a,"a"],[b,"b"],[c,"c"]]:
            if cnt >0:
                heapq.heappush(maxheap,[-cnt,letter])
        while maxheap:
            cnt,letter =heapq.heappop(maxheap)
            if len(ans)>=2 and ans[-1]==ans[-2]==letter:
                if not maxheap:
                    break 
                count,letterx=maxheap.pop()
                count+=1
                ans+= letterx
                if count<0:
                    heapq.heappush(maxheap,[count,letterx])
                heapq.heappush(maxheap,[cnt,letter])
            else:
                ans+= letter
                cnt+=1
                if cnt<0:
                    heapq.heappush(maxheap,[cnt,letter])
        return ans 


if __name__=="__main__":
    instance=Solution()
    # instance.longestDiverseString(1,2,3)
    # instance.longestDiverseString(0,5,3)
    # instance.longestDiverseString(0,5,0)
    # instance.longestDiverseString(0,5,0)
    # instance.longestDiverseString(0,8,11)
    # instance.longestDiverseString(0,2,2)
    instance.longestDiverseString(0,4,7)
                
            

            
            


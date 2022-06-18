from typing import Optional ,List
class Solution:
    def maxProfit_1(self, prices: List[int]) -> int:
        # 存在数学上的单调性
        # 1,3,5,7,6,5,9
        xstack=[]
        ans=0
        for price in prices:
            if not xstack:
                xstack.append(price)
            elif xstack[-1]<price:
                ans+=price-xstack[-1]
            xstack=[price]
        return ans 
    def maxProfit(self, prices: List[int]) -> int:
        # 存在数学上的单调性
        # 1,3,5,7,6,5,9
        bottom_price=prices[0]

        ans=0
        for price in prices:
            if bottom_price<price:
                ans+=price-bottom_price
            bottom_price=price
        return ans 

if __name__ == "__main__":
    instance=Solution()
    print(instance.maxProfit([1,3,5,7,6,5,9]))
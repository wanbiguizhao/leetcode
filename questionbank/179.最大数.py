from typing import List
class Solution:
  	def largestNumber(self, nums: List[int]):
		def compare(a:int,b:int):
			return str(a)+str(b)>str(b)+str(a)
      	sorted(nums,key=compare,)
      
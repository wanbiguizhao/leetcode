from typing import List 
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
       
        def _letter_combinations(digits_index,pre_str):
            if digits_index==const_digits_len:
                ans.append(pre_str)
                return 
            number_value=digits[digits_index]
            for letter in mapping_info[number_value]:
                _letter_combinations(digits_index+1,pre_str+letter)
        if not digits:
           return []
        mapping_info={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        const_digits_len=len(digits)
        ans=[]
        _letter_combinations(0,"")
        return ans 
if __name__ == "__main__":
    instance = Solution()
    print(instance.letterCombinations(""))
    print(instance.letterCombinations("2433"))


from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=Counter(nums)
        majority=0
        maxnum=0    
        for key,value in d.items():
            
            if value>maxnum:
                maxnum=value
                majority=key
        return majority

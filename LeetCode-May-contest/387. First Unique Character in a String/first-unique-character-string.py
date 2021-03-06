
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s)==0:
            return -1
        table=collections.Counter(s)       
        for i in range(len(s)):           
            if table[s[i]]==1:
                return i           
        return -1

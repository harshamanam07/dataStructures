# Time Complexity O(N)-->O(ransomNote+magazine)
# Space O(N) -->(worst case)--> ransom note unique characters

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        table=Counter(magazine)
        for char in ransomNote:
            if table[char]<=0 or char not in table:
                return False
            table[char]-=1
                
        return True
                
            
                
            

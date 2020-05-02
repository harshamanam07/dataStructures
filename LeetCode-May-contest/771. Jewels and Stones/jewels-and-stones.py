# Runs in O(N) and space is O(N)
# Memory beats 97% but space is bad

from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # Create a Dict for each charcter and count it
        table=Counter([char for char in S])
        # return the sum of dict values of charcters in jewel strings present in stones dictionary
        return sum(table[x] for x in J)

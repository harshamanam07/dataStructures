# Ask if all versions are true.

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start=1
        end=n
        
        while(start<=end):
            mid=((end-start)//2)+start
            
            if isBadVersion(mid)==False:
                start=mid+1
            else:
                end=mid-1
        return start

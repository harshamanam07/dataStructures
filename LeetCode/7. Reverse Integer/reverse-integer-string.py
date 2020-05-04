class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            neg=-1
        else:
            neg=1        
        x=int(str(abs(x))[::-1])
        
        if int(x)< 2147483648:
            return int(x)*neg
        else:
            return 0

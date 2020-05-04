# old way...converting to string not allowed
# overflow condition check


class Solution:
    def reverse(self, x: int) -> int:
        num=x
        reversenum=0
        if num<0:
            neg=-1
        else:
            neg=1
        num=abs(num) 
        
        while abs(num)>0:
            reversenum=reversenum * 10 +num%10
            num=num//10
        reversenum*=neg
        #check overflow > 2^32
        if abs(reversenum) <2147483648:
            return reversenum
        else:
            return 0

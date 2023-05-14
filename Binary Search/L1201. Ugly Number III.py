'''
find the nth ugly number 
an ugly number is defined as a number which is divisible by a or b or c

num//a -> gives the numbers which are divisible by a before num
lcm(a,b) -> gives numbers which are divisible by both a and b (intersection)

if we have three numbers a, b and c and we need to find the nth number hich is divisible by either
of them problem is that number which is divisible might get repeated to avoid this we subtract
this part of three (a,b) (b,c) (c,a) to get numbers which are common
but we might erase count of a number which is common to all three of them
to avoid this we add lcm(a,lcm(b,c)) -> num common to (a,b,c)


'''
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # can calculate gcd and lcm from same code (imp) 
        def lcm(num,den):
            num1, num2 = num, den
            if num<den:
                num, den = den, num
            rem = num%den
            while rem!=0:
                num = den
                den = rem
                rem = num%den
            gcd = den
            return (num1*num2)//gcd
        
        def enough(num):
            total = num//a + num//b + num//c - num//lcm(a,b) - num//lcm(b,c) - num//lcm(c,a) + num//lcm(a,lcm(b,c))
            return total>=n
        
        left, right = 1, 10**10
        while left<right:
            mid = left + (right - left)//2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left
        
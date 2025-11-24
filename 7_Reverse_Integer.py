import math


class Solution(object):
    def reverse(self, x):
        MIN = -2**31
        MAX = 2**31 -1
        res =0
        is_neg = False

        if x <0:
            is_neg = True
        x = abs(x)    


        while x>0:
            digit = x %10
            x = x//10
            res = (res*10)+digit
    

        if is_neg:
            res = -res         
        print(res)    
        if(res >= MAX or res<= MIN):
            return 0
        else:
            return res 
        
# o(log(x))
# 21ms        










class Solution(object):
    def reverse(self, x):
        MIN = -2**31
        MAX = 2**31 -1

        is_neg = x<0
        x = abs(x)
        res =0

        while x>0:
            digit = x%10
            x = x//10

            if(res > MAX//10 or (res == MAX and digit >= MIN%10)):
                return 0
            # if(res <MIN //10 or (res == MIN and digit <= MIN%10)):
            #     return 0
            res = (res*10)+ digit

        if is_neg:
            return -res
        else:
            return res    






class Solution(object):
    def reverse(self, x):
        MIN = -2**31
        MAX = 2**31 -1

        res =0

        while x:
            digit = int(math.fmod(x,10))

            x = int(x/10)

            if(res > MAX//10 or (res == MAX //10 and digit >= MAX%10)):
                return 0
            if(res <MIN //10 or(res == MIN//10 and digit <= MIN%10)):
                return 0
            res = (res*10)+ digit

  
        print(res)
        return res    
  
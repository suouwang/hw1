import math

def average(nums):
    sum = float(0)
    for i in nums:
        sum+=i
    return sum/len(nums)

def power(base, exponent):
    return math.pow(base,exponent)

def sqrt(num):
    if num<0:
         return "ValueError"
    else:
        return math.sqrt(num)
    
def log(num,base=10):
    if ((num<=0) or (base<=0)):
         return "ValueError"
    else:
        return math.log(num,base)
#is divisible checks whether num is divisible by every integer between divisor and max_divisor
#num is the number to check the divisibility of
#divisor is the first number to check divisibility by (usually 2)
#max divisor is the highest number that num must be divisible by
#the function checks divisibility by every number between divisor and max divisor
#True is returned if num is divisible by all divisors
def is_divisible(num,divisor,max_divisor):
    if divisor == max_divisor+1:
        return True
    if num % divisor == 0:
        return is_divisible(num,divisor+1,max_divisor)
    else:
        return False
    
#find_lowest returns the smallest integer for which is_divisible returns true
#num is the first number to check, if is_divisible returns false, 
#we continue to increment num by 1 until True is returned

def find_lowest(num,divisor,max_divisor):
    if is_divisible(num,divisor,max_divisor) == True:
        return num
    else:
        return find_lowest(num+1,divisor,max_divisor)

#for i in range(12252240,1000000000):
#    if is_divisible(i,2,19):
#        print(i)

#the answer is 232792560

#I cheated a bit by multiplying the answer for 18 by 19 to save computation time
print(12252240*19)
